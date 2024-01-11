from django.db import models
from django.urls import reverse


#А оно для хранения моделей для представления данных из базы данных

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=30)
    course_slug = models.SlugField(max_length=255, db_index=True, unique=True)
    def get_absolute_url(self):
        return reverse('lesson', kwargs={'course_slug': self.course_slug})

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    lesson_name = models.CharField(max_length=50)
    lesson_number = models.SmallIntegerField()
    lesson_content = models.TextField(blank=True)
    lesson_slug = models.SlugField(max_length=255, db_index=True, unique=True)
    def get_absolute_url(self):
        return reverse('lesson', kwargs={'lesson_slug': self.lesson_slug})



class Test(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.PROTECT)
    question = models.CharField(max_length=100)
    answer_1 = models.CharField(max_length=100)
    answer_2 = models.CharField(max_length=100)
    answer_3 = models.CharField(max_length=100)
    answer_4 = models.CharField(max_length=100)
    correct = models.SmallIntegerField()

