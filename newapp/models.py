from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Index

class ActivityTheme(models.Model):
    name = models.CharField("Название вида деятельности", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид деятельности"
        verbose_name_plural = "Виды деятельности"
        ordering = ['name']

class Company(models.Model):
    REGION_CHOICES = [
        ('Россия', 'Россия'),
        ('Франция', 'Франция'),
        ('Германия', 'Германия'),
        ('США', 'США'),
        ('Китай', 'Китай'),
        ('Япония', 'Япония'),
        ('Великобритания', 'Великобритания'),
        ('Италия', 'Италия'),
        ('Испания', 'Испания'),
        ('Канада', 'Канада'),
    ]

    name = models.CharField("Название", max_length=255, unique=True)
    short_name = models.CharField("Краткое название", max_length=50, blank=True, unique=True)
    region = models.CharField("Страна", max_length=100, choices=REGION_CHOICES)
    priority = models.IntegerField(
        "Приоритет",
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    website = models.URLField("Ссылка на сайт", blank=True)
    email = models.EmailField("Email", blank=True)
    activity_themes = models.ManyToManyField(
        ActivityTheme,
        verbose_name="Виды деятельности",
        blank=True
    )
    additional_contacts = models.TextField(
        "Доп. сведения",
        blank=True,
        help_text="Формат: Тип:значение (например, Telegram:@example)"
    )

    def clean(self):
        if Company.objects.filter(name__iexact=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Компания с таким названием уже существует'})
        
        if self.short_name and Company.objects.filter(short_name__iexact=self.short_name).exclude(pk=self.pk).exists():
            raise ValidationError({'short_name': 'Компания с таким кратким названием уже существует'})

    def save(self, *args, **kwargs):
        if not self.short_name:
            self.short_name = self.generate_short_name()
        self.full_clean()
        super().save(*args, **kwargs)
    
    def generate_short_name(self):
        return ''.join([word[0].upper() for word in self.name.split()[:3]])

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ['name']
        indexes = [
            Index(fields=['name']),
            Index(fields=['short_name']),
            Index(fields=['additional_contacts']),  # Добавляем индекс для поиска
        ]