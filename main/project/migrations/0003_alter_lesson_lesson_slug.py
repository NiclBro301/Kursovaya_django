# Generated by Django 4.2.5 on 2024-01-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_lesson_lesson_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
