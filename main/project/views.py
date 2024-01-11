from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.db import models

from project.models import Lesson, Course, Test

# Create your views here.

header = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Курсы', 'url_name': 'courses'},
        {'title': 'Помощь', 'url_name': 'help'},
        {'title': 'О проекте', 'url_name': 'about'}
        ]
def home(request):
    data = {'header': header}
    return render(request, 'home/home.html', context=data)


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


def lesson_list(request, course_slug):
    course = {'Vvedenie': 1, 'Drugoy': 2}
    try:
        obj = Lesson.objects.all()
    except Lesson.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    slug = get_object_or_404(Course, course_slug=course_slug)
    lessons = Lesson.objects.filter(course_id=course[course_slug])

    data = {'header': header,
            'lesson': obj,
            'slug': slug,
            'lesson_list': lessons}
    print(obj)
    return render(request, 'lesson/lesson_list.html', context=data)


def first(request):
    answer = 0
    correct = '1'
    next = 'second'
    previous = 'first'
    lesson = ['Введение', 'Добро-пожаловать на курс по языку программирования Python!']
    test = ['Python - это язык...?', 'Программирования', 'Английский',
            'Литературный', 'Тела']

    if request.method == 'POST':
        answer = request.POST.get('answer', '')

    data = {'header': header,
            'test': test,
            'lesson': lesson,
            'answer': answer,
            'correct': correct,
            'next': next,
            'previous': previous,
            }
    return render(request, 'lesson/lesson.html', context=data)


def second(request):
    answer = 0
    correct = '3'
    next = 'third'
    previous = 'first'
    lesson = ['Продолжение', 'Чтобы вывести на экран что-нибудь используют функцию print()']
    test = ['Что нужно использовать, чтобы вывести текст на экран?', 'Молитвы', 'Воспитание',
            'Функцию print()', 'Вежливость']

    if request.method == 'POST':
        answer = request.POST.get('answer', '')

    data = {'header': header,
            'test': test,
            'lesson': lesson,
            'answer': answer,
            'correct': correct,
            'next': next,
            'previous': previous,
            }
    return render(request, 'lesson/lesson.html', context=data)

def third(request):
    answer = 0
    correct = '2'
    next = 'third'
    previous = 'second'
    lesson = ['Конец', 'Поздравляем, вы изучили язык программирования Python!!!']
    test = ['Вам понравился наш курс??', 'Нет', 'Очень!',
            'Безвкусно', 'Не понравился']

    if request.method == 'POST':
        answer = request.POST.get('answer', '')

    data = {'header': header,
            'test': test,
            'lesson': lesson,
            'answer': answer,
            'correct': correct,
            'next': next,
            'previous': previous,
            }
    return render(request, 'lesson/lesson.html', context=data)
def something(request):
    answer = 0
    correct = '4'
    next = 'something'
    previous = 'something'
    lesson = ['[ПРОБНЫЙ УРОК]', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi dolor doloremque dolores magnam maxime minus nesciunt, repellat soluta sunt unde?']
    test = ['Введите правильный ответ', 'False', 'False',
            'False', 'True']

    if request.method == 'POST':
        answer = request.POST.get('answer', '')

    data = {'header': header,
            'test': test,
            'lesson': lesson,
            'answer': answer,
            'correct': correct,
            'next': next,
            'previous': previous,
            }
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


