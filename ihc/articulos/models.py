from django.db import models
from categorias.models import Categoria

# Create your models here.
class Articulo(models.Model):
	ArtCod		= models.CharField(verbose_name='Código del artículo', max_length=15, primary_key=True)
	ArtNom		= models.CharField(verbose_name='Nombre', max_length=30)
	ArtDes		= models.CharField(verbose_name='Descripción', max_length=100, blank=True, null=True)
	ArtImg		= models.ImageField(verbose_name='Imagen', upload_to='pics/articles', blank=True, null=True)
	ArtCatCod	= models.ForeignKey(Categoria, verbose_name='Categoría', on_delete=models.CASCADE)
	ArtCosUni	= models.DecimalField(verbose_name='Costo unitario', max_digits=5, decimal_places=2)
	ArtSitAct	= models.BooleanField(verbose_name='Disponible', default=True)
	ArtSto		= models.IntegerField(verbose_name='Cantidad en stock', default=1)

	def __str__(self):
		return self.ArtNom
