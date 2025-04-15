from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы и атрибуты для всех полей
        self.fields['name'].widget.attrs.update({
            'class': 'form-control mb-3',
            'placeholder': 'Введите название компании'
        })
        self.fields['region'].widget.attrs.update({
            'class': 'form-control mb-3',
            'placeholder': 'Введите регион'
        })
        self.fields['priority'].widget.attrs.update({
            'class': 'form-control mb-3',
            'min': '1',
            'max': '10'
        })
        self.fields['contacts'].widget.attrs.update({
            'class': 'form-control mb-3',
            'rows': '3',
            'placeholder': '{"phone": "+7 999 123-45-67", "email": "example@mail.com"}'
        })
        self.fields['activity_themes'].widget.attrs.update({
            'class': 'form-control mb-3',
            'placeholder': 'IT, Маркетинг, Производство'
        })

    class Meta:
        model = Company
        fields = ['name', 'region', 'priority', 'contacts', 'activity_themes']
        labels = {
            'name': 'Название компании',
            'region': 'Регион',
            'priority': 'Приоритет (от 1 до 10)',
            'contacts': 'Контактная информация (JSON)',
            'activity_themes': 'Виды деятельности'
        }
        help_texts = {
            'contacts': 'Введите данные в JSON-формате',
            'activity_themes': 'Укажите через запятую'
        }
        