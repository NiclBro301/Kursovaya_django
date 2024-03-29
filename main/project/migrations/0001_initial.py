# Generated by Django 4.2.5 on 2023-12-19 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=50)),
                ('lesson_number', models.SmallIntegerField()),
                ('lesson_content', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.course')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer_1', models.CharField(max_length=100)),
                ('answer_2', models.CharField(max_length=100)),
                ('answer_3', models.CharField(max_length=100)),
                ('answer_4', models.CharField(max_length=100)),
                ('correct', models.SmallIntegerField()),
                ('lesson', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='project.lesson')),
            ],
        ),
    ]
