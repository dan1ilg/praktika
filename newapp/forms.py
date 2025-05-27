from django import forms
from django.core.exceptions import ValidationError
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
                 'website', 'email', 'activity_themes', 'additional_contacts']
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
            'website': forms.URLInput(attrs={
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
            'region': 'Страна',
            'short_name': 'Краткое название',
            'activity_themes': 'Виды деятельности',
            'website': 'Ссылка на сайт'
        }
        help_texts = {
            'additional_contacts': 'Каждый контакт с новой строки'
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        short_name = cleaned_data.get('short_name')
        instance = getattr(self, 'instance', None)

        if name:
            qs = Company.objects.filter(name__iexact=name)
            if instance and instance.pk:
                qs = qs.exclude(pk=instance.pk)
            if qs.exists():
                self.add_error('name', 'Компания с таким названием уже существует')

        if short_name:
            qs = Company.objects.filter(short_name__iexact=short_name)
            if instance and instance.pk:
                qs = qs.exclude(pk=instance.pk)
            if qs.exists():
                self.add_error('short_name', 'Компания с таким кратким названием уже существует')

        return cleaned_data