from django.shortcuts import render
from .models import Usuario
from django.views import generic
# Create your views here.

class listUsuarios(generic.ListView):
	template_name="usuario/lista_usuarios.html"
	model=Usuario
