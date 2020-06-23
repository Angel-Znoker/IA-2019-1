"""Programa extra. Clasificador estadístico a priori

Autores:  	
	Hernández García Luis Angel
	Vázquez Sánchez Ilse Abril

Fecha de entrega: 28 de Noviembre del 2018"""

import numpy as np
import math

""" La siguiente función obtiene la matriz de varianza-covarianza de una muestra """
def matrizCovarianza(muestra):
	n = len(muestra)
	# Transformamos la matriz de datos a una matriz de desviación de datos llamada desv
	# Se hace uso de la fórmula a = A - 11'A(1/n)
	unos = np.ones([n, n])
	desv = muestra - unos.dot(muestra)*(1/n)
	# Luego, para encontrar la matriz de sumas de la desviación de cuadrados, se calcula a'a 
	sumDesv = desv.getT().dot(desv)
	# Finalmente, se obtiene la matriz de covarianzas
	mCov = sumDesv * (1/n)
	return mCov

""" Utilizamos esta función para determinar la media de los vectores de muestra dados, se regresa
una matriz con las medias de los componentes de los datos dados """
def media(puntos):
	return np.mean(np.matrix(puntos), axis = 0)

""" La siguiente función regresa el determinante de una matriz, la cual debe ser declarada como
numpy.matrix """
def determinante(matriz):
	return(np.linalg.det(matriz))

""" Con esta función obtenemos el resultado de multiplicar -1/2 por la matriz de covarianzas
inversa para, posteriormente, obtener el primer término de la expresión """
def primerTermino(C):
	cI = C.getI()
	return (-1/2)*cI

""" Con esta función obtenemos la multiplicación de la matriz de covarianzas inversa por la matriz
de medias, para después, obtener el segundo término de la expresión """
def segundoTermino(m, C):
	cI = C.getI()
	mT = m.getT() 
	return(cI.dot(mT).getT())

""" Obtenemos el resultado del primer término de la expresión, el cual posteriormente será sumado
al logaritmo del determinante de la matriz de covarianzas por -1/2 """
def tercerTermino(m, C):
	mT = m.getT()
	cI = C.getI()
	return((-1/2) * m.dot(cI).dot(mT))

""" Con esta función simulamos la multiplicación de la matriz de covarianzas por el vector 
genérico (transpuesto y no transpuesto) y, simplificamos los términos semejantes obtenidos """
def imprimeA(a, n):
	aux = ""
	for l in range(n**2):
		for p in range(l, n):
			if l == p:
				suma = a.item(l, p)
				aux += str('%.4f' % suma)+'x'+str(l)+'^2'+'+'
			else:
				suma = a.item(l, p) + a.item(p, l)
				aux += str('%.4f' % suma)+'x'+str(l)+'x'+str(p)+'+'
	return aux

""" Con esta función simulamos la multiplicación de la matriz de covarianzas por la de medias por el 
vector genérico """
def imprimeB(b, n):
	aux = ""
	for i in range(n):
		aux += str('%.4f' % b.item(i))+'x'+str(i)+'+'
	return aux

""" Con esta función imprimimos el término independiente de la expresión"""
def imprimeC(c):
	return(str('%.4f' % c.item(0)))

""" La siguiente función calcula las funciones discriminantes de un conjunto de datos.
Recibe la lista de muestras y la dimensión de los vectores que las componen.
Da como resultado un string que contiene las funciones calculadas"""
def aPriori(datos, n):
	C = []
	m = []
	det = []
	f = ""
	# Obtenemos las matrices de covarianza, las medias de las muestras y los determinantes
	for i, muestras in enumerate(datos):
		f += '\nfd'+str(i)+'(X) = '
		# Obtenemos las medias de las muestras
		m.append(media(muestras))
		# Obtenemos la matriz de covarianzas de las muestras
		C.append(matrizCovarianza(np.matrix(muestras)))
		# Obtenemos el determinante de la matriz de covarianzas
		det.append(determinante(C[i]))

		# Obtenemos cada uno de los elementos que compondrán a la función discriminante
		f+= imprimeA(primerTermino(C[i]), n)
		f+= imprimeB( segundoTermino(m[i], C[i]), n)
		f+= imprimeC(tercerTermino(m[i], C[i]) + (-1/2) * math.log(det[i]))
	return f

datos1 = [[[1, 2], [2, 2], [3, 1], [2, 3], [3,2]], [[8, 10], [9, 8], [9, 9], [8, 9], [7,9]]]
# n es la dimensión de los vectores que componen las muestras
n1 = 2
print(aPriori(datos1, n1))

datos2 = [[[0.5, 10.5],[1, 12.5],[3, 10.5],[3, 12.5],[3, 14.5],[3, 18],[5, 18],[5, 16],[5, 14.5],[5, 13]], [[6, 9],[8, 10],[9, 11],[8.5, 12],[7, 13.5], [8, 16]]]
n2 = 2
print(aPriori(datos2, n2))