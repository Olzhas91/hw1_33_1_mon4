from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def postListView(request):
    post_value = models.Post.objects.all()
    return render(request, 'post/post.html', {'post_key': post_value})

def helloView(request):
    return HttpResponse('<h1>Добро пожаловать. Это мои проект.</h1>')

def now_dataView(request):
    return HttpResponse('<h1>Сейчас 2023 год.</h1>')

def goodbyView(request):
    return HttpResponse('<h1>Досвидание. До скорой встречи.</h1>')

def postDetailView(request, id):
    post_id = get_object_or_404(models.Post, id=id)
    return render(request, 'post/post_detail.html', {'post_id': post_id})
