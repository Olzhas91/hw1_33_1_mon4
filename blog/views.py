from django.shortcuts import render
from django.http import HttpResponse

def helloView(request):
    return HttpResponse('<h1>Добро пожаловать. Это мои проект.</h1>')

def now_dataView(request):
    return HttpResponse('<h1>Сейчас 2023 год.</h1>')

def goodbyView(request):
    return HttpResponse('<h1>Досвидание. До скорой встречи.</h1>')
