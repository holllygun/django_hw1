import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    path = 'C:/Users/pushk/Desktop/django_1/app'
    lst = os.listdir(path)
    res = []
    for i, item in enumerate(lst):
        res.append(f'{i+1}) {item} ')
    res = "\n".join(res)
    res1 = []
    path1 = 'C:/Users/pushk/Desktop/django_1/first_project'
    lst1 = os.listdir(path1)
    for i, item in enumerate(lst1):
        res1.append(f'{i+1}) {item} ')
    res1 = "\n".join(res1)
    total_res = (f'app: {res}; first_project: {res1}')

    return HttpResponse(total_res)
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # raise NotImplemented
