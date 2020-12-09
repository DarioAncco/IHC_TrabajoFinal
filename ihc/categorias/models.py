from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
	CatCod		= models.CharField(verbose_name='Código de categoría', max_length=10, primary_key=True)
	CatDes		= models.CharField(verbose_name='Descripción', max_length=30)
	CatImg		= models.ImageField(verbose_name='Imagen', upload_to='pics/categories', null=True, blank=True)

	def __str__(self):
		return self.CatDes
