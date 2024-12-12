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
        fields = ['name', 'county']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Institution Name'}),
            'county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter County'}),
        }
