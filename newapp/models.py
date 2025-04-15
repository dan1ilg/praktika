from django.db import models
import json

class Company(models.Model):
    name = models.CharField("Название", max_length=255)
    region = models.CharField("Регион", max_length=100)
    priority = models.IntegerField("Приоритет", default=0)

# JSON-поля для гибких атрибутов
    contacts = models.JSONField(default=dict) 
    activity_themes = models.JSONField(default=list)

    def __str__(self):
        return self.name
