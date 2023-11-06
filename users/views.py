from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == 'GET':
        context_data = {
            'from': RegisterForm
        }
        return render(request, 'users/register.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = RegisterForm(data)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            if cleaned_data.get('password1') == cleaned_data.get('password2'):
                User.objects.create_user(
                    username=cleaned_data.get('username'),
                    password=cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'Простите, попробуйте еще раз')

        context_data = {
            'form': form
        }
        return render(request, 'users/register.html', context=context_data)


def login_view(request):
    if request.method == 'GET':
        context_data = {
            'from': LoginForm
        }

        return render(request, 'users/login.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            if user:
                login(request, user)
                return redirect('/post')
            else:
                form.add_error('password1', 'Простите, попробуйте еще раз')

        context_data = {
            'form': form
        }
        return render(request, 'users/login.html', context=context_data)


def logout_view(request):
    logout(request)
    return redirect('/post')
