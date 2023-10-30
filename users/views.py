from django.shortcuts import render,redirect
from .models import MyUser,Cart,Historic
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login as logon, logout as logouts
from . forms import *
from django.contrib.auth.decorators import permission_required,login_required
from PIL import Image


#RENDER DEFS
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
        return render(request,'signup.html')




#AUTH DEFS
def logout(request):
    if request.user.is_authenticated:
        logouts(request)
        return redirect('main')
    else:
        messages.add_message(request, constants.WARNING,'Você precisa estar logado')
        return redirect('main')
    
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
                messages.add_message(request, constants.WARNING, 'Login ou senha incorretos ')
                return redirect('render_login')
            elif user is not None:
                logon(request, user)
                name = request.user.first_name
                messages.add_message(request, constants.SUCCESS, f'Bem vindo {name}!')
                return redirect('main')
        except:
            messages.add_message(request, constants.WARNING, 'Erro interno do sistema')
            return redirect('main')
def auth_register(request):
    if request.method != 'POST':
        messages.add_message(request, constants.WARNING,'Método HHTP incorreto')
        return redirect('render_register')
    else:
        try:
            name = request.POST.get('name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            conf_pass = request.POST.get('conf_pass')
            
            if(password != conf_pass):
                messages.add_message(request, constants.WARNING, 'Senhas não correspondem')
                return redirect('render_register')
            elif(len(password) <8 or len(password.strip())==0):
                messages.add_message(request, constants.WARNING, 'Sua senha deve ter ao mínimo 8 dígitos')
                return redirect('render_register')
            elif(len(username.strip()) == 0):
                messages.add_message(request, constants.WARNING, 'Preencha corretamente o usuário')
                return redirect('render_register')
            user = MyUser.objects.filter(username = username)
            if(len(user) > 0):
                messages.add_message(request,constants.ERROR,'Já existe um usuário com este nome!')
                return redirect('render_register')
            elif(len(user) == 0):
                name = name.capitalize()
                last_name = last_name.capitalize()
                user = MyUser(
                            username = username,
                            email = email,
                            first_name = name,
                            last_name = last_name)
                user.set_password(password)
                user.save()
                logon(request, user)
                cart = Cart(user = request.user)
                historic = Historic(user = request.user)
                historic.save()
                cart.save()
                messages.add_message(request, constants.SUCCESS,f'Muito obrigado por se juntar a nós {name} {last_name}, aproveite!')
                return redirect('main')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('main')

@login_required(login_url='render_login')
def new_profile_pic(request):
    if request.method == 'POST':
        file = request.FILES.get('picture') 
        user = MyUser.objects.get(username = request.user.username)
        user.profile_pic = file
        user.save()
        messages.add_message(request, constants.INFO, "Sua imagem foi alterada com sucesso!")
        return redirect('render_profile')
    else:
        messages.add_message(request, constants.INFO, "Método HHTP inválido!")
        return redirect('main')

    

