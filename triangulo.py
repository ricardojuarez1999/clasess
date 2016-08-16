from figura import FiguraGeometrica
class Triangulo(FiguraGeometrica):

	def __init__(self, base, altura):
		super().__init__(base, altura)

	def imprimir(self):
		resultado = ""

		for i in range(self.altura):
			resultado += "\n" + " " * (self.altura - i) + " *" * (i + 1)
		return resultado

	def calcular_area(self):
		return super().calcular_area() / 2.0