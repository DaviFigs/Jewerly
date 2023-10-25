from django.shortcuts import render, redirect
from .forms import FormProduct
from django.contrib.messages import constants
from django.contrib import messages

def prod_register(request):
    form =FormProduct()
    alter_input = ('name', "price","description","amount","amount","category")
    for i in alter_input:
        if i in alter_input:
            form.fields[i].widget.attrs['class']='form-control'
            form.fields[i].widget.attrs['placeholder']=f'{i}'
    context = {
        'form':form
    }
    return render(request, 'prod_form.html', context)

def auth_prod_register(request):
    if request.method != 'POST':
        messages.add_message(request,constants.ERROR,'Método HHTP inválido')
        return redirect('main')
    else:
        pass



