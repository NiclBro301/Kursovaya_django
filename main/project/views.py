from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models

from project.models import Lesson, Course, Test

# Create your views here.

header = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Личный кабинет', 'url_name': 'reg'},
        {'title': 'Курсы', 'url_name': 'courses'},
        {'title': 'Помощь', 'url_name': 'help'},
        {'title': 'О проекте', 'url_name': 'about'}
        ]
def home(request):
    data = {'header': header}
    return render(request, 'home/home.html', context=data)

def registration(request):
    data = {'header': header}
    raise Http404()

def courses(request):
    try:
        obj = Course.objects.all()
    except Course.DoesNotExist:
        raise Http404("No MyModel matches the given query.")


    data = {'header': header,
            'course': obj}

    print(obj)
    return render(request, 'courses/courses.html', context=data)

def help(request):
    data = {'header': header}
    return render(request, 'help/help.html', context=data)

def about(request):
    data = {'header': header}
    return render(request, 'about/about.html', context=data)

def lesson_list(request, lesson_slug):
    course = {'Vvedenie': 1, 'Drugoy': 2}
    try:
        obj = Lesson.objects.all()
    except Lesson.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    slug = get_object_or_404(Course, course_slug=lesson_slug)
    lessons = Lesson.objects.filter(course_id=course[lesson_slug])

    data = {'header': header,
            'lesson': obj,
            'slug': slug,
            'lesson_list': lessons}
    print(obj)
    return render(request, 'lesson/lesson_list.html', context=data)


def lesson(request, lesson_slug):
    try:
        obj = Lesson.objects.get()
    except Lesson.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    slug = get_object_or_404(Course, course_slug=lesson_slug)

    data = {'header': header,
            'lesson': obj,
            'slug': slug}
    print(obj)
    return render(request, 'lesson/lesson.html', context=data)

#------------------------------------------------------------------------------------

def pageNotFound(request, exception):
    data = {'header': header,
            'error': 'Ошибка 404: такой страницы нет :('}
    return render(request, 'exceptions/error.html', context=data)


def serverError(request):
    data = {'header': header,
            'error': 'Ошибка 500: сервер сломался, скоро починю :('}
    return render(request, 'exceptions/error.html', context=data)
def badRequest(request, exception):
    data = {'header': header,
            'error': 'Ошибка 400: Сайт не может прожевать ваш запрос :('}
    return render(request, 'exceptions/error.html', context=data)
def forbidden(request, exception):
    data = {'header': header,
            'error': 'Ошибка 403: Страница заброшена или перемещена по другому адресу :('}
    return render(request, 'exceptions/error.html', context=data)


