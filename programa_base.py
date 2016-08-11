from cuadrado import Cuadrado
from triangulo import Triangulo
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
			cuadrado = Cuadrado(datos)
			print ("""
	1. Calcular area.
	2. imprimir.""")
			opcion2 = int(input("ingrese su opcion: "))
			if opcion2 == 1:
				print ("el area es: ", cuadrado.calcular_area())
			elif opcion2 == 2:
				print (cuadrado.imprimir())
			else:
				print ("esa opcion no es valida")
		elif opcion1 == 2:
			datos = int(input("ingrese base: "))
			datos2 = int(input("ingrese altura: "))
			triangulo = Triangulo(datos,datos2)
			print ("""
	1. Calcular area.
	2. imprimir.""")
			opcion2 = int(input("ingrese su opcion: "))
			if opcion2 == 1:
				print ("el area es: ", triangulo.calcular_area())
			elif opcion2 == 2:
				print (triangulo.imprimir())
			else:
				print ("esa opcion no es valida")
		else:
			print ("esa opcion no es valida")
	elif opcion == 2:
		respuesta = False
	else:
		print ("esa opcion no es valida...")