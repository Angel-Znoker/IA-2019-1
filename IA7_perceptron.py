""" Heaviside es la funcion escalon que describe cuando ocurrirá el proceso de activación, simulando neuronas
	Recibe: z que es una combinación lineal de entradas x y pesos w
	Devuelve: El valor de activación
"""
def Heaviside(z, umbral):
	if(z >= umbral): return 1
	return -1

""" calculo_z es la función que calculará la z que posteriormente será evaluada en la función de Heaviside
	Recibe: El renglón de la tabla con el que se está trabajando y el vector de pesos
	Devuelve: z evaluado en la función Heavisisde
"""
def calculo_z(renglon, pesos, umbral):
	suma = 0
	renglon = renglon_mod(renglon)
	for i in range(len(renglon)):
		suma = suma + (renglon[i] * pesos[i])
	return Heaviside(suma, umbral)

""" cambio_pesos realiza el cambio en el vector pesos después de realizar un paso
	Recibe: El vector de pesos, el paso calculado en la iteración, el renglón de la tabla trabajado
	Devuelve: el vector de pesos con el paso agregado
"""
def cambio_pesos(pesos, paso, renglon):
	renglon = renglon_mod(renglon)
	for i in range(len(renglon)):
		pesos[i] = pesos[i] + (renglon[i] * paso)
	return pesos

""" renglon_mod es una función auxiliar que agrega un 1 al primer elemento del vector y elimina la salida definida en la tabla
	Recibe: una lista
	Devuelve: lista modificada
"""
def renglon_mod(renglon):
	renglon = renglon[0:(len(renglon) - 1)]
	renglon.insert(0, 1)
	return renglon

""" Perceptron es el algoritmo encargado de modificar los pesos de acuerdo a los dato conocidos, se 
	detiene cuando después de la iteración ya no existe un cambio en el vector de pesos
	Devuelve: Lista de pesos finales
"""
def Perceptron(tabla, pesos, n, umbral):
	#Datos iniciales
	#Ejemplo con Nand
	while(1):
		aux_pesos = pesos.copy()
		#Se hace el cambio del peso para cada relnglón de la tabla
		for i in tabla:
			paso = n * (i[len(tabla[0]) - 1] - calculo_z(i, pesos, umbral))
			pesos = cambio_pesos(pesos, paso, i)
		print("pesos: ", pesos)
		if(aux_pesos == pesos): return pesos

def main():
	tabla = [[0,0,1], [0,1,1], [1,0,1], [1,1,-1]]
	pesos = [0] * len(tabla[0])
	n = 0.1
	umbral = 0
	print("\nPesos: ", Perceptron(tabla, pesos, n, umbral))

main()