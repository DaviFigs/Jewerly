from django.shortcuts import render,redirect
from .models import MyUser
from django.contrib.messages import constants
from django.contrib import messages
from . forms import *

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
    pass
