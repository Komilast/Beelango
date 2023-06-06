from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as log
from django.contrib.auth.models import User
from .forms import RegisterForm


def home(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'main/welcome.html')
    else:
        pass


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log(request, user)
            return redirect('home')
        else:
            attr = {
                'error_message': 'Неверные имя пользователя или пароль',
                'title': 'Вход в Beelango'
            }
            return render(request, 'main/login.html', attr)
    else:
        attr = {
            'error_message': '',
            'title': 'Вход в Beelango'
        }
        return render(request, 'main/login.html', attr)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']


    return render(request, 'main/register.html', {'form':})
