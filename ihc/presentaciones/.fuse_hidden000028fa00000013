from django.urls import path

from .views import (
	PresentacionListView,
	PresentacionCreateView,
	PresentacionUpdateView,
	PresentacionDeleteView,
	)

urlpatterns = [
	path("listarPresentacion", PresentacionListView.as_view(), name="Listar_Presentacion"),
	path("crearPresentacion", PresentacionCreateView.as_view(), name="Crear_Presentacion"),
	path("<pk>/editar", PresentacionUpdateView.as_view(), name="Editar_Presentacion"),
	path("<pk>/borrar/", PresentacionDeleteView.as_view(), name="Eliminar_Presentacion"),
	]
