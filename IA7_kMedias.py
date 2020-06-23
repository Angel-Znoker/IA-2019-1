import numpy

""" Esta función realiza el calculo de las nuevas k-medias
	recibe: m: numpy.array (medias)
			p: numpy.array (puntos)
"""
def nuevaMedia(m, p):
	# Se calcula la distancia de un punto con cada una de las medias
	a = [0 for x in range(len(m))] # almacena las distancias de un punto a las medias
	b = [[] for x in range(len(m))] # almacena los puntos más cercanos a cada media
	for i in range(len(p)):
		for j in range(len(m)):
			a[j] = numpy.sqrt(numpy.sum((p[i] - m[j]) ** 2)) # Distancia
		b[a.index(min(a))].append(p[i]) # Se ve la menor distancia y se guarda con su media correspondiente
	# Calculo de la nueva media promedio
	aux = numpy.zeros(len(m[0]), dtype = float)
	for i in range(len(m)):
		for j in range(len(b[i])):
			aux = aux + b[i][j]
		m[i] = aux * (1/len(b[i]))
		aux = numpy.zeros(len(m[0]), dtype = float)

""" Función que implementa el algoritmo de k-medias
	recibe: m: numpy.array (medias)
			p: numpy.array (puntos)
"""
def kMedias(m, p):
	converge = False
	i = 0
	while not converge:
		# Mientras el algoritmo no converja se calcula la nueva media con la
		# función nueva media
		mAux = numpy.copy(m)
		# la función nuevaMedia modifica a 'm' sin necesidad de retornar su valor
		nuevaMedia(m, p)
		i += 1
		print("\niteracion " + str(i) + ":")
		print(m)
		if numpy.array_equal(mAux, m):
		# cuando la media anterior sea igual a la nueva media se termina el cálculo
			converge = True

""" Función que calcula la media inicial. Se calcula el punto más cercano al origen
	y las k-1 medias más lejanas a él
	recibe: p: numpy.array (puntos)
			k int
	regresa: m: numpy.array (medias)
"""
def calculaMedias(p, k):
	disCentro = [0 for x in range(len(p))] # lista que almacenara la distancia de los puntos al centro
	# calculo de la distancia de los puntos al origen y obtención del más cercano (primer media)
	for i in range(len(p)):
		disCentro[i] = numpy.sqrt(numpy.sum((p[i] - 0) ** 2))
	m = [p[disCentro.index(min(disCentro))]]

	b = [0 for x in range(len(p))] # lista que almacenará las distancias de los puntos a la primer media
	# calculo de la distancia de los puntos a la primer media
	for i in range(len(p)):
		b[i] = numpy.sqrt(numpy.sum((p[i] - m[0]) ** 2))

	# se ordenan las distancias de mayor a menor y se obtienen las k-1 medias más lejanas
	c = b.copy()
	c.sort(reverse = True)
	for i in range(k - 1):
		m.append(p[b.index(c[i])])

	return m


def main():
	p = numpy.array([[8, 10], [3, 10.5], [7, 13.5], [5, 18], [5, 13], [6, 9], [9, 11], [3, 18], [8.5, 12], [8, 16]], dtype = float)
	m = numpy.array(calculaMedias(p, 2), dtype = float)
	#m = numpy.array([[8,10], [5, 13]], dtype = float)

	print("Media inicial:\n", m)

	kMedias(m, p)

	print("\nMedia final:\n", m)

main()