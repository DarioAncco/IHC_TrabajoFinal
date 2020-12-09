from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
	UsuNom	= models.OneToOneField(User, verbose_name='Nombre de usuario', primary_key=True, on_delete=models.CASCADE)

	Masculino = 'M'
	Femenino = 'F'
	sexo_del_usuario = [
		(Masculino, 'Masculino'),
		(Femenino, 'Femenino'),
	]

	UsuSex		= models.CharField(verbose_name='Sexo del trabajador', max_length=1, choices=sexo_del_usuario, default=Masculino, null=True, blank=True)

	UsuFecNac	= models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
	UsuDNI		= models.CharField(verbose_name='DNI', max_length=15, null=True, blank=True, unique=True)
	UsuTel		= models.CharField(verbose_name='Teléfono de contacto', max_length=15, null=True, blank=True)

	class Meta:
		verbose_name_plural='Perfiles de Usuario'

	def __str__(self):
		return self.UsuNom.first_name + ' ' + self.UsuNom.last_name
