from django import forms
from .models import Question, Option
from .models import Institution


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

class SponsorEventForm(forms.Form):
    sponsor_name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sponsor_email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    donation_amount = forms.DecimalField(label='Donation Amount', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label='Message to the Event Organizers')

    def clean_donation_amount(self):
        amount = self.cleaned_data['donation_amount']
        if amount <= 0:
            raise forms.ValidationError('Donation amount must be greater than zero.')
        return amount