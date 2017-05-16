678from django.db import models

# Create your models here.
class Estudiantes(models.Model):
	"""."""

	nombres=models.CharField(max_length=200)
	apellidos=models.CharField(max_length=200)
	edad=models.IntegerField(default=0)
	grado=models.ForeignKey('grado.Grados')

	def __str__(self):
		"""."""
		return "%s %s - %s" % (
			self.nombres,
			self.apellidos,
			self.grado)