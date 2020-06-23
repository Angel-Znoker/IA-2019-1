"""Programa extra. Algoritmo de la red bayesiana

Autores:  	
	Hernández García Luis Angel
	Vázquez Sánchez Ilse Abril

Fecha de entrega: 28 de Noviembre del 2018"""

from itertools import product

""" Con esta clase creamos los nodos de la red bayesiana, los cuales contienen cada uno su propia tabla
que contiene las probabilidades conjuntas """
class vertice:
	def __init__(self, nombre):
		self.id = nombre
		self.padres = []
		self.tabla = {}

	""" Esta tabla corresponde a la tabla de probabilidad conjunta perteneciente al nodo. Esta tabla está 
	representada mediante un diccionario cuyas claves son tuplas con los valores booleanos de las variables
	de las que depende el nodo y sus valores son listas con la probabilidad de que ocurra o no el evento 
	representado por el nodo"""
	def agregaTabla(self, tabla):
		self.tabla = tabla
	
	""" Los padres correspoden a la lista de nodos de los que depende el nodo """
	def agregaPadre(self, padre):
		self.padres = padre

"""	Con esta clase creamos la gráfica de la red bayesiana """
class redBayesiana:
	def __init__(self):
		self.vertices = {}

	""" Este método sirve para crear nodos de la red bayesiana, por lo que recibe el nombre del nodo, su tabla
	de verdad y la lista de vértices de los cuales depende su valor de probabilidad"""
	def agregarVertice(self, v, informacion):
		if v not in self.vertices:
			vert = vertice(v)
			self.vertices[v] = vert

			for a, b in informacion.items():
				if a == "Tabla":
					vert.agregaTabla(b)
				elif a == "Padres":
					vert.agregaPadre(b)

	""" Con este método obtenemos los valores de los sumandos para obtener la probabilidad conjunta a partir de la
	expansión de la función de probabilidad conjunta y las probabilidades conjuntas de las tablas de cada nodo"""
	def probTabla(self, nodos, valores):
		pos, val, res = {True: 0, False: 1}, [], 1
		# Analizamos cada uno de los nodos que se utilizarán para obtener el valor del sumando
		for a in nodos:
			#Obtenemos su posición dentro de la lista de nodos, la cual utilizaremos para obtener su valor booleano dentro de la lista valores
			j = nodos.index(a)
			for b in self.vertices[a].padres:
				# Obtenemos la posición del padre del nodo que se está analizando y su valor booleano lo agregamos a la lista val para crea la tupla con la que obtendremos la probabilidad conjunta del nodo
				i = nodos.index(b) 
				val.append(valores[i])
			# Obtenemos la probabilidad conjunta del nodo analizado y lo multiplicamos con las demás probabilidades conjuntas
			res *= self.vertices[a].tabla[tuple(val)][pos[valores[j]]]
			val = []
		# Regresamos el valor del sumando
		return res

	""" Con este método obtenemos la probabilidad P(A|B). Para lo cual, recibimos el nombre del nodo A y B y sus respectivos
	valores booleanos"""
	def probConjunta(self, Ap, Av, Bp, Bv):
		lista = [Bp]+self.vertices[Bp].padres
		valNum, valDen, num, den = [], [], 0, 0

		# Con estos dos ciclos obtenemos la lista de nodos de los cuales depende la probabilidad P(B|A)
		for a in lista:
			for b in self.vertices[a].padres:
				if b not in lista:
					lista.append(b)

		# Posteriormente, obtenemos los valores booleanos dados para cada nodo. Para el caso del numerador, dejamos constantes los valores
		# recibidos para A y B y, para el denominador, solamente es constante el de B y, para los demás nodos, agregamos None
		valNum = [Av if x is Ap else Bv if x is Bp else None for x in lista]
		valDen = [Bv if x is Bp else None for x in lista]

		# A partir de las listas creadas anteriormente, le damos valores de True o False a aquellos valores que quedaron con valor None
		valNum = product(*[[True, False] if x is None else [x] for x in valNum])
		valDen = product(*[[True, False] if x is None else [x] for x in valDen])
		
		# Para cada una de las listas obtenidas en el paso anterior, obtenemos la probabilidad conjunta para el denominador y el numerador
		for a in valNum:
			num += self.probTabla(lista, a)
		
		for b in valDen:
			den += self.probTabla(lista, b)

		# Regresamos el valor de la probabilidad conjunta
		return num/den

	def P(self, Ap, Av, Bp, Bv):
		resultado = self.probConjunta(Ap, Av, Bp, Bv)
		print("P("+Ap+"="+str(Av)+"|"+Bp+"="+str(Bv)+") = "+"{0:.2f}".format(resultado*100)+"%")

class main:
	# PRUEBA 1. EJEMPLO DE PDF DEL PROFESOR
	# Lluvia
	Lluvia = {		"Tabla" : {(): [0.2, 0.8]},
					"Padres": []}
	# Aspersor
	Aspersor = { 	"Tabla" : {	(True,): [0.01, 0.99],
								(False,): [0.4, 0.6]},
					"Padres": ["Lluvia"]}

	# PastoMojado
	PastoMojado = {	"Tabla": {	(True, True): [0.99, 0.01],
								(True, False): [0.9, 0.1],
								(False, True): [0.8, 0.2],
								(False, False): [0.0, 1.0]},
	 				"Padres": ["Aspersor", "Lluvia"]}

	rb1 = redBayesiana()
	rb1.agregarVertice("Aspersor", Aspersor)
	rb1.agregarVertice("Lluvia", Lluvia)
	rb1.agregarVertice("PastoMojado", PastoMojado)

	rb1.P("Lluvia", True, "PastoMojado", True)

	# PRUEBA 2. EJERCICIO DE EXAMEN PARCIAL 2
	Nublado 	= {	"Tabla" : {	(): [0.5, 0.5]},
					"Padres" : []}

	Aspersor	= {	"Tabla": {	(True,): [0.1, 0.9],
								(False,): [0.5, 0.5]},
					"Padres": ["Nublado"]}

	Lluvia 		= {	"Tabla": { 	(True,): [0.8, 0.2],
								(False,): [0.2, 0.8]},
					"Padres": ["Nublado"]}

	PastoMojado = {	"Tabla": {	(True, True): [0.99, 0.01],
								(True, False): [0.9, 0.1],
								(False, True): [0.9, 0.1],
								(False, False): [0.0, 1.0]},
	 				"Padres": ["Aspersor", "Lluvia"]}

	rb2 = redBayesiana()
	rb2.agregarVertice("Nublado", Nublado)
	rb2.agregarVertice("Aspersor", Aspersor)
	rb2.agregarVertice("Lluvia", Lluvia)
	rb2.agregarVertice("PastoMojado", PastoMojado)

	rb2.P("Nublado", True, "PastoMojado", True)