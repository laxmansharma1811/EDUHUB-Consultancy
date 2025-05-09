from django import forms
from .models import *

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['name', 'email', 'phone', 'country', 'program', 'message']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Basic phone validation (adjust as needed)
        if not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
            raise forms.ValidationError("Phone number must contain only digits, +, -, or spaces.")
        return phone
    



class PartnerApplicationForm(forms.ModelForm):
    class Meta:
        model = PartnerApplication
        fields = ['name', 'email', 'company', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Your Email'}),
            'company': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Your Company (Optional)'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Tell us about your partnership goals', 'rows': 5}),
        }