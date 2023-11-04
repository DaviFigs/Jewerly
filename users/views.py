from django.shortcuts import render,redirect
from .models import MyUser,Cart,Historic
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login as logon, logout as logouts
from . forms import *
from django.contrib.auth.decorators import permission_required,login_required
from products.models import Product


#RENDER DEFS

def render_login(request):
    try:
        if request.user.is_authenticated:
            messages.add_message(request, constants.WARNING, 'Você já está logado!')
            return redirect('main')
        else:
            return render(request, 'login.html')
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')
    
def render_register(request):
    try:
        if request.user.is_authenticated:
            messages.add_message(request, constants.WARNING, 'Você já está logado!')
            return redirect('main')
        else:
            return render(request,'signup.html')
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')

@login_required(login_url='render_login')
def render_alter_pass(request):
    try:
        return render(request, 'alter_pass.html')
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')



#AUTH DEFS
@login_required(login_url='render_login')
def logout(request):
    try:
        logouts(request)
        return redirect('main')
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')
    
def auth_login(request):
    try:
        if request.method != 'POST':
            messages.add_message(request, constants.WARNING, 'Método HTTP inválido')
            return redirect('main')
        else:  
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
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')
        
def auth_register(request):
    try:
        if request.method != 'POST':
            messages.add_message(request, constants.WARNING,'Método HHTP incorreto')
            return redirect('render_register')
        else:
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
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')

@login_required(login_url='render_login')
def new_profile_pic(request):
    try:
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
    except:
        messages.add_message(request,constants.ERROR, 'Erro inesperado, tente novamente')
        return redirect('main')
    

@login_required(login_url='render_login')
def alter_data(request):
    try:
        if request.method == 'POST':
            user = MyUser.objects.get(username = request.user.username)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            
            user.first_name = first_name.capitalize()
            user.last_name = last_name.capitalize()
            user.email = email
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Seus dados foram alterados com sucesso!')
            return redirect('render_profile')
        else:
            messages.add_message(request, constants.INFO, 'Método HHTP inválido!')
            return redirect('main')
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente')
        return redirect('main')

@login_required(login_url='render_login')
def alter_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            current_pass = request.POST.get('current_pass')
            new_pass = request.POST.get('new_pass')
            conf_pass = request.POST.get('conf_pass')
            user = authenticate(username = username, password = current_pass)
            if user != None:
                if new_pass == conf_pass:
                    if len(new_pass) <8 or len(new_pass.strip())==0:
                        messages.add_message(request, constants.WARNING, 'A senha deve conter no mínimo 8 caracteres')
                        return redirect('render_alter_pass')
                    else:
                        user.set_password(new_pass)
                        user.save()
                        messages.add_message(request, constants.SUCCESS, 'Sua senha foi alterada com sucesso')
                        logouts(request)
                        return redirect('render_login')
                else:
                    messages.add_message(request, constants.WARNING, 'As senhas estão diferentes')
                    return redirect('render_alter_pass')
            else:
                messages.add_message(request, constants.WARNING, 'Usuário ou senha inválidos!')
                return redirect('render_alter_pass')
        else:
            messages.add_message(request, constants.WARNING, 'Método HTTP inválido!')
            return redirect('main')
    except:
        messages.add_message(request,constants.ERROR, 'Erro inesperado, tente novamente')
        return redirect('main')


def add_product_on_cart(request, id):
    #try:
        if request.method ==  'GET':
            cart = Cart.objects.get(user = request.user)
            product = Product.objects.get(id = id)
            cart.product.add(product)
            cart.save
            return redirect(f'/main_view/product/{id}')
        else:
            messages.add_message(request, constants.WARNING, 'Método HTTP inválido')
            return redirect('main')
    #except:
        #messages.add_message(request, constants.WARNING, 'Erro inesperado')
        #return redirect('main')
