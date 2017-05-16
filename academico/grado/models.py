from django.db import models

# Create your models here.
class Grados(models.Model):
	nombre=models.CharField(max_length=200)
	orden=models.IntegerField(default=0)

	def __str__(self):
		return self.nombre