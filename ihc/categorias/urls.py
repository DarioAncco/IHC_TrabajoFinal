from django.urls import path

from . import views

urlpatterns = [
	path("registroCategoria",views.registroCategoria,name="registroCategoria"),
	path("mostrarCategoria",views.mostrarCategoria,name="mostrarCategoria"),
	path("actualizarCategoria/<str:id>",views.actualizarCategoria,name="actualizarCategoria"),
	path("eliminarCategoria/<str:id>",views.eliminarCategoria,name="eliminarCategoria"),
	path("",views.categoriaHome,name="Categoria"),
	
]