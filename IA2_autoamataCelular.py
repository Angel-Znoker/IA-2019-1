"""Versión de Python utilizada 3.7.0 (Recomendado utilizar la consola de Linux o cmd en Windows)

	Integrantes:
	- Aco Guerrero Iván Rogelio
	- Ricardo Hernández Gómez
	- Hernández Arrieta Carlos Alberto
	- Hernández García Luis Angel

	Éste es un programa que simula el comportamiento de un autómata celular unidimensional;
	en cada celda hay un organismo vivo "*" ó muerto " " y con las siguientes reglas de evolución:
	- Cada organismo vivo sobrevivirá la siguiente etapa si y solo si no lo rodean por ambos lados
	otros organismos vivos (por inanición, representación de la competencia).
	- En una celda vacía aparece un organismo vivo si al menos un vecino es un organismo vivo
	(división celular).

	El programa solicita 2 datos, el primero es la población inicial que puede ser un sólo organismo 
	vivo u otra en la que la población inicial es aleatoria.

	Este comportamiento se obtuvo de la tabla del automata celular visto en clase(pag 9)
	http://dicyg.fi-c.unam.mx:8080/lalo/ia/presentaciones/introduccion-a-la-inteligencia-artificial

	Tambien se encuentra como la regla 126 de Wolfram
	http://mathworld.wolfram.com/Rule126.html
"""

from random import randint

def calculo(arreglo):
	"""
	Aquí se simula el estado del organismo (vivo o muerto).
	Arreglo es una cadena de tres elementos donde el elemento central es al que se le analizará su estado
	según las condiciones establecidas.

	Args:
		arreglo: String
	Returns:
		Regresa un "1" en caso de estar vivo o un "0" en caso de estar muerto
	"""
	# Se toma cada uno de los elementos del arreglo y se convierten a enteros.
	a = int(arreglo[0])
	b = int(arreglo[1])
	c = int(arreglo[2])
	# Se regresa el resulatado de la ecuación, para obtener el estado que 
	# tendrá el elemento en el siguiente nivel. El tipo de dato regresado
	# es string.
	return str((a + b + (a * b) + c + (a * c) + (b * c)) % 2)

def imprimeLinea(arreglo):
	"""
	Imprime el nivel correspondiente al Triángulo de Sierpinski proporcionado por arreglo

	Args:
		arreglo: String
	"""
	espacios = " " * (75 - int(len(arreglo)/2)) # Espacios necesarios antes de imprimir la linea
	# Se reemplazan los "1" con "*" y los "0" con espacios
	arreglo = arreglo.replace("0"," ").replace("1","*")
	print(espacios + arreglo)

def sierpinski(arreglo):
	"""
	Procesa el siguiente nivel del Triángulo de Sierpinski

	Args:
		arreglo: String (nivel actual del triángulo)
	Returns:
		aux: String (nivel siguiente del triángulo)
	"""
	aux = ""
	# Los ceros son necesarios para realizar el calculo inicial y final
	# del siguiente nivel. Por ejemplo: con el arreglo inicial "1",
	# necesitaremos tener "00100", esto con el fin de tener los bloques
	# "001", "010" y "100" y obtener el resultado "111"
	arreglo = "00" + arreglo + "00"
	# En este for se envian bloques de 3 del arreglo, para obtener
	# el estado siguiente de la celda central.
	for x in range(len(arreglo) - 2):
		aux += calculo(arreglo[x:x+3])
	# Se hace un limite para que las lineas solo sean de maximo 143 caracteres de largo
	# (Solo es necesario para presentacion en la pantalla)
	if len(aux) >= 143:
		return aux[1:len(aux)-1]
	else:
		return aux

def main():
	"""Función principal main

	Esta Función tiene dos opciones:
	La Primera es iniciar con un arreglo con un único elemento inicial o con elementos aleatorios
	La segunda es que altura quieres que tenga el Triángulo de Sierpinski a imprimir
	"""
	print("**** Triangulo de Sierpinski ****")
	print("Escoja una opcion:\n1. Iniciar con un solo elemento\n2. Iniciar con un numero aleatorio")
	opcion = input("Opcion: ")
	print("\nEscoja la altura")
	altura = input("Altura: ")

	if opcion == "1":
		arreglo = "1"
	else:
		# El numero aleatorio es un numero entero de entre 2 a 2^64,
		# es convertido a binario y convertido a string. La conversión
		# a binario genera un numero con el prefijo "0b", el cual es
		# eliminado antes de asignarlo a la variable arreglo
		arreglo = str(bin(randint(2, 18446744073709551616)))[2:]

	for i in range(int(altura)):
		# El estado actual de los elementos se imprime antes de
		# de calcular su siguiente.
		imprimeLinea(arreglo)
		arreglo = sierpinski(arreglo)

main()
