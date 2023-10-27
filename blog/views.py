from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def post_list_view(request):
    if request.method == 'GET':
        post_value = models.Post.objects.all()

        context_data = {
            'post_key': post_value
        }

        return render(request, 'post/post.html', context=context_data)

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Добро пожаловать. Это мои проект.</h1>')

def now_data_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Сейчас 2023 год.</h1>')

def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Досвидание. До скорой встречи.</h1>')

def post_detail_view(request, id):
    if request.method == 'GET':
        post = get_object_or_404(models.Post, id=id)

        context_data = {
            'post': post
        }
        return render(request, 'post/post_detail.html', context=context_data)

