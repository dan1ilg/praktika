from django import forms
from .models import Company, ActivityTheme

class CompanyForm(forms.ModelForm):
    activity_themes = forms.ModelMultipleChoiceField(
        queryset=ActivityTheme.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label="Виды деятельности"
    )

    class Meta:
        model = Company
        fields = ['name', 'short_name', 'region', 'priority', 
                 'website', 'email', 'activity_themes', 'additional_contacts']  # Изменено с phone на website
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полное название компании'
            }),
            'short_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автогенерация, если оставить пустым'
            }),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10
            }),
            'website': forms.URLInput(attrs={  # Новое поле для сайта
                'class': 'form-control',
                'placeholder': 'https://example.com'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@domain.com'
            }),
            'additional_contacts': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Telegram:@username\nVK:https://vk.com/username'
            }),
        }
        labels = {
            'short_name': 'Краткое название',
            'activity_themes': 'Виды деятельности',
            'website': 'Ссылка на сайт'  # Новый label
        }
        help_texts = {
            'additional_contacts': 'Каждый контакт с новой строки'
        }