from django.shortcuts import render
from estudiante.models import Estudiantes
# Create your views here.
def lista_estudiantes(request):
	"""."""
	estudiantes = Estudiantes.objects.all()
	return render(request, 'estudiantes_lista.html', {
		'estudiantes': estudiantes
		})