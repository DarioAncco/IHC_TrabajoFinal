from django.urls import path
from . import views

urlpatterns = [
	path("registroArticulo",views.registroArticulo , name="registroArticulo"),
	path("listaArticulo",views.listaArticulo , name="registrarCompra"),
	path("registroCompra",views.registrarCompra , name="registrarCompra"),
	path("listaCompra",views.listaCompra , name="registrarCompra"),
	path('',views.articulosCompras , name="articulos")
]