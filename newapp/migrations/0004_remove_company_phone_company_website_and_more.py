# Generated by Django 5.1.7 on 2025-05-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_activitytheme_alter_company_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='phone',
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, verbose_name='Ссылка на сайт'),
        ),
        migrations.AlterField(
            model_name='company',
            name='region',
            field=models.CharField(choices=[('Москва', 'Москва'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Новосибирск', 'Новосибирск'), ('Екатеринбург', 'Екатеринбург'), ('Казань', 'Казань')], max_length=100, verbose_name='Регион'),
        ),
    ]
