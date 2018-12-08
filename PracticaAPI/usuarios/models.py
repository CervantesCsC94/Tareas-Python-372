from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre=models.CharField(max_length=100)
	#Apellido=models.CharField(max_length=250)
	timestap=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre

