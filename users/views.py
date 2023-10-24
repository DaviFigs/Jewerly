from django.shortcuts import render,redirect
from .models import MyUser
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login as logon, logout as logouts
from . forms import *

def logout(request):
    if request.user.is_authenticated:
        logouts(request)
        return redirect('main')
    else:
        messages.add_message(request, constants.WARNING,'Você precisa estar logado')
        return redirect('main')
def render_login(request):
    if request.user.is_authenticated:
        messages.add_message(request, constants.WARNING, 'Você já está logado!')
        return redirect('main')
    else:
        return render(request, 'login.html')
def render_register(request):
    if request.user.is_authenticated:
        messages.add_message(request, constants.WARNING, 'Você já está logado!')
        return redirect('main')
    else:
        return render(request,('signup.html'))
    
def auth_login(request):
    if request.method != 'POST':
        messages.add_message(request, constants.WARNING, 'Método HTTP inválido')
        return redirect('main')
    else:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            if user == None:
                messages.add_message(request, constants.WARNING, f'Login ou senha incorretos {user}')
                return redirect('render_login')
            elif user is not None:
                logon(request, user)
                messages.add_message(request, constants.SUCCESS, 'Login efetuado com sucesso')
                return redirect('main')
        except:
            messages.add_message(request, constants.WARNING, 'Erro interno')
            return redirect('main')
def auth_register(request):
    if request.method != 'POST':
        messages.add_message(request, constants.WARNING,'Método HHTP incorreto')
        return render_register(request)
    else:
        try:
            name = request.POST.get('name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            conf_password = request.POST.get('conf_password')
            #continuar a criação dos usuários


        except:
            messages.add_message(request, constants.ERROR, 'Erro do sistema')
            return redirect('main')
