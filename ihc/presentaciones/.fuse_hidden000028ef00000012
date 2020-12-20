from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Presentacion
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
	)

# Create your views here.

class PresentacionListView(ListView):
	model = Presentacion

class PresentacionCreateView(CreateView):
	model = Presentacion
	fields = [
		'PreCod',
		'PreDes',
		]

class PresentacionUpdateView(UpdateView):
	model = Presentacion
	fields = [
		'PreCod',
		'PreDes',
		]
	template_name_suffix = '_edit'

class PresentacionDeleteView(DeleteView):
	model = Presentacion
	success_url = reverse_lazy('Listar_Presentacion')
	template_name_suffix = '_delete'
