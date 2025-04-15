from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'region', 'priority', 'contacts', 'activity_themes']
        
    contacts = forms.CharField(widget=forms.Textarea, help_text='Введите JSON: {"phone": "", "email": ""}')
    activity_themes = forms.CharField(help_text='Введите через запятую: IT, Маркетинг')