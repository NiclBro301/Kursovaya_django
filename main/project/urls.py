"""
URL configuration for coolsite project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from  project.models import *

from project.views import *

urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('help/', help, name='help'),
    path('about/', about, name='about'),
    path('lesson/<slug:course_slug>/', lesson_list, name='lesson'),
    path('first/', first, name='first'),
    path('second/', second, name='second'),
    path('third/', third, name='third'),
    path('something/', something, name='something'),
]


