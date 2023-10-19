from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from . import models

def postListView(request):
    post_value = models.Post.objects.all()
    return render(request, 'printer/printer.html', {'post_key': post_value})

def helloView(request):
    return HttpResponse('<h1>Добро пожаловать. Это мои проект.</h1>')

def now_dataView(request):
    return HttpResponse('<h1>Сейчас 2023 год.</h1>')

def goodbyView(request):
    return HttpResponse('<h1>Досвидание. До скорой встречи.</h1>')
