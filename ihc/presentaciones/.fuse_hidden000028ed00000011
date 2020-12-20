from django.db import models
from django.urls import reverse

# Create your models here.
class Presentacion(models.Model):
	PreCod		= models.CharField(verbose_name='Código de la presentación', max_length=10, primary_key=True)
	PreDes		= models.CharField(verbose_name='Descripción', max_length=20)

	class Meta:
		verbose_name_plural = 'Presentaciones'

	def __str__(self):
		return self.PreDes

	def get_absolute_url(self):
		return reverse('Editar_Presentacion',kwargs={'pk': self.PreCod})
