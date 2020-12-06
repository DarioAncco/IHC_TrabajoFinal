from django.urls import path
from . import views

urlpatterns = [
	path("registroArticulo",views.registroArticulo , name="registroArticulo"),
]