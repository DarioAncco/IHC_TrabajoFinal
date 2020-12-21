from django.urls import path

from . import views

urlpatterns = [
	path("comprar",views.registroCompra,name="registroCompra"),
	
]