from django.shortcuts import render, redirect
from .forms import FormProduct
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import permission_required,login_required
#Can add product - ID: 41 - add_product
#@permission_required('add_logentry', login_url='/base/main/')
#user.user_permissions.add(74) Adiciona permissão conforme id


#RENDER DEFS
@permission_required('add_product', login_url='render_login')
def prod_register(request):
    try:
        form =FormProduct()
        alter_input = ('name', "price","description","amount","amount","category","image")
        for i in alter_input:
            if i in alter_input:
                if i == "description":
                    form.fields[i].widget.attrs['class'] = 'form-control size-desc'
                    form.fields[i].widget.attrs['placeholder']=f'Product {i}'
                else:
                    form.fields[i].widget.attrs['class']='form-control'
                    form.fields[i].widget.attrs['placeholder']=f'Product {i}'
        context = {
            'form':form
        }
        return render(request, 'prod_form.html', context)
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')


#AUTH DEFS
def auth_prod_register(request):
    try:
        if request.method == 'POST':
            form = FormProduct(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form.clean()
                messages.add_message(request, constants.SUCCESS, 'Produto cadastrado com sucesso!')
                return redirect('form_prod')
            else:
                context = {
                    'form':form
                }
                return redirect('form_prod',context)
        else:
            messages.add_message(request,constants.ERROR,'Método HHTP inválido')
            return redirect('form_prod')
    except:
        messages.add_message(request,constants.ERROR, 'Erro inesperado, tente novamente')
        return redirect('main')


