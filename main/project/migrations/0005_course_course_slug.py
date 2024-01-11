# Generated by Django 4.2.5 on 2024-01-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_lesson_lesson_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
