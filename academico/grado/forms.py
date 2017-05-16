from django import forms
from grado.models import Grados
class GradoForm(forms.ModelForm):
	class Meta:
		model=Grados
		fields = [
		'nombre',
		'orden'
		]