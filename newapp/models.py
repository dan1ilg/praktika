from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ActivityTheme(models.Model):
    name = models.CharField("Название вида деятельности", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид деятельности"
        verbose_name_plural = "Виды деятельности"

class Company(models.Model):
    REGION_CHOICES = [
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
        ('Новосибирск', 'Новосибирск'),
        ('Екатеринбург', 'Екатеринбург'),
        ('Казань', 'Казань'),
    ]

    name = models.CharField("Название", max_length=255)
    short_name = models.CharField("Краткое название", max_length=50, blank=True)
    region = models.CharField("Регион", max_length=100, choices=REGION_CHOICES)
    priority = models.IntegerField(
        "Приоритет",
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    website = models.URLField("Ссылка на сайт", blank=True)  # Изменено с phone на website
    email = models.EmailField("Email", blank=True)
    activity_themes = models.ManyToManyField(
        ActivityTheme,
        verbose_name="Виды деятельности",
        blank=True
    )
    additional_contacts = models.TextField(
        "Доп. контакты",
        blank=True,
        help_text="Формат: Тип:значение (например, Telegram:@example)"
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.short_name:
            self.short_name = self.generate_short_name()
        super().save(*args, **kwargs)
    
    def generate_short_name(self):
        return ''.join([word[0].upper() for word in self.name.split()[:3]])

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ['name']