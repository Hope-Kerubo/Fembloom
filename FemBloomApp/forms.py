from django import forms
from .models import Question, Option
from .models import Institution, SponsorEvent


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            options = question.options.all()
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[(option.id, option.text) for option in options],
                widget=forms.RadioSelect
            )




class DonationApplicationForm(forms.Form):
    DONATION_CHOICES = [
        ('products', 'Menstrual Products'),
        ('money', 'Financial Support'),
        ('sponsorship', 'Program Sponsorship'),
    ]

    PRODUCT_CHOICES = [
        ('sanitary_pads', 'Sanitary Pads'),
        ('tampons', 'Tampons'),
        ('menstrual_cups', 'Menstrual Cups'),
        ('hygiene_kits', 'Hygiene Kits'),
    ]

    donation_type = forms.ChoiceField(
        choices=DONATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Select Donation Type"
    )
    products = forms.ChoiceField(
        choices=PRODUCT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
        label="Select Products (if applicable)"
    )
    institution = forms.ModelChoiceField(
        queryset=Institution.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Select Institution"
    )



class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'county','address','contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Institution Name'}),
            'county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter County'}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Address'}),
            'contact': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Contact'}),
        }

class SponsorEventForm(forms.ModelForm):
    class Meta:
        model = SponsorEvent
        fields = ['sponsor_name', 'sponsor_email', 'donation_amount', 'message']
        widgets = {
            'sponsor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sponsor_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'donation_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean_donation_amount(self):
        amount = self.cleaned_data['donation_amount']
        if amount <= 0:
            raise forms.ValidationError('Donation amount must be greater than zero.')
        return amount