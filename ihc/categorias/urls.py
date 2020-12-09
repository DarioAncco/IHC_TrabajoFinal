from django.urls import path

from . import views

urlpatterns = [
	path("registroCategoria",views.registroCategoria,name="registroCategoria"),
	]