from cuadrado import cuadrado
from triangulo import triangulo
respuesta = True
while respuesta == True:
	datos = None
	print ("""
	1. Crear una figura.
	2. salir.""")
	opcion = int(input("ingrese su opcion: "))
	if opcion == 1:
		print ("""
	1. Crear cuadrado.
	2. Crear triangulo.""")
		opcion1 = int(input("ingrese su opcion: "))
		if opcion1 == 1:
			datos = int(input("ingrese lado: "))
			print ("""
	1. Crear cuadrado.
	2. Crear triangulo.""")
		elif opcion1 == 2:

		else:
			print ("esa opcion no es valida")
	elif opcion == 2:

	else:
		print ("esa opcion es invalida")