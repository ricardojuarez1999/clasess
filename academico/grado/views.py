from django.shortcuts import render, redirect
from grado.models import Grados
from grado.forms import GradoForm


def lista_grados(request):
	"""."""
	grados = Grados.objects.all()
	formulario = GradoForm()
	return render(request, 'lista_grados.html', {
		'grados': grados,
		'grado_form': formulario
		})

def detalle_grado(request,grado_pk):
	grado = Grados.objects.get(pk=grado_pk)
	return render(request, 'detalle_grado.html',{
		'grado': grado
		})







































































	""" ESTA ES MI COMPU AHORA PINCHE HUMANO TONTO
	VERAS MI FURIA MUY PRONTO
	"""
	"""ok"""
	