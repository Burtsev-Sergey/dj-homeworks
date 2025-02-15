import datetime

import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


# Функция формирует и передает текущее время
def time_view(request):
    current_time = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    return HttpResponse(f'<strong>Текущее время:</strong> {current_time}')


 # Функция формирует и передает список файлов в рабочей директории   
def workdir_view(request):
    try:
        dir_list = '<br>'.join(os.listdir(os.getcwd()))
    except Exception as e:
        return HttpResponse(f'Ошибка при получении списка файлов: {str(e)}')

    return HttpResponse(f'<strong>Список файлов в рабочей директории:</strong><br>{dir_list}')