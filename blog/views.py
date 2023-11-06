from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models
from .forms import ProductCreateForm
from .models import Post


def post_list_view(request):
    if request.method == 'GET':
        post_value = models.Post.objects.all()

        context_data = {
            'post_key': post_value,
            'user': request.user
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


def product_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm
        }

        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            Post.objects.create(
                image=cleaned_data.get('image'),
                title=cleaned_data.get('title'),
                description=cleaned_data.get('description'),
                type_printer=cleaned_data.get('type_printer'),
                cost=cleaned_data.get('cost'),
            )
            return redirect('/post/')

        return render(request, 'products/create.html', context={'form': form})
