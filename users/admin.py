from django.contrib import admin
from django.contrib.auth import admin as adm
from . models import MyUser
from .forms import UserCreationForm, UserChangeForm

@admin.register(MyUser)
class MyUserAdmin(adm.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = MyUser
    fieldsets = adm.UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields' :("cpf", "past_buys")}),
        )#Adicionamos ao fiedsets os campos adicionais que criamos no user
    readonly_fields = ("cpf", "past_buys", )