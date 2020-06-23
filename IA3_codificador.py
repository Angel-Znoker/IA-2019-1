"""Versión de Python utilizada 3.6.X

	Integrantes:
		- Aco Guerrero Iván Rogelio
		- Hernández Arrieta Carlos Alberto
		- Hernández García Luis Angel
		- Hernández Gómez Ricardo
	
	Este programa realiza el cifrado y descifrado de mensajes por columna (cifrado por transposición
	columnar simple https://goo.gl/MSQQLt). Para ello se requiere de una palabra clave o llave que
	ayudara a relizar dichas acciones. El proceso de cifrado viene descrito en las páginas 6, 7 y 8
	del documento Capitulo 1: Agentes inteligentes y ambientes (https://goo.gl/cH8zB4).

	El programa solicita dos datos: el mensaje y la clave, además de escoger entre las opciones de
	cifrar o descifrar el menaje.

"""
from math import ceil

def cryptographer(oText, key):
	"""
	Esta función realiza el cifrado del mensaje dado, de acuerdo al proceso descrito.
	Recibe el mensaje y la clave y regresa el mensaje cifrado.
	Args:
		originalText: String
		key: String
	Returns:
		mensaje: String
	"""
	sectionsOrd = []
	seenLetter = None

	#Preparación de la cadena:
	oText = oText.strip().replace(" ","")

	#Si el texto es más corto que la llave:
	if len(key) > len(oText):
		oText += oText[-1]*(len(key)-len(oText))

	#Añadido de caracteres extras al final:
	auxC = (len(oText)/len(key))
	oText += oText[-1]*int(float("%.1f" %((ceil(auxC)-auxC)*len(key))))

	#Proceso:
	sectionsV = [oText[i::len(key)] for i in range(len(key))]
   
	for letter in sorted(key):
		if letter == seenLetter:
			auxIndex = key.find(letter, auxIndex+1)
		else:
			auxIndex = key.find(letter)
		seenLetter = letter
		sectionsOrd.append(sectionsV[auxIndex])

	return ''.join(sectionsOrd)

def decipher(cText, key):
	"""
	Aquí se realiza la decodificación o el descifrado del mensaje, utilizando el proceso antes descrito.
	Al igual que la funcoón cryptographer, recibe el mensaje y la clave y regresa el mensaje descifrado.
	Args:
		ciphText: String
		key: String
	Returns:
		mensaje: String
	"""
	sectionsOrd, seenLetters = [],[]

	auxCount = int(len(cText)/len(key))
	sectionsV = [cText[i:i+auxCount] for i in range(0, len(cText), auxCount)] 
	
	for letter in key:
		auxIndex = ''.join(sorted(key)).find(letter)
		while auxIndex in seenLetters:
			auxIndex+=1
		seenLetters.append(auxIndex)
		sectionsOrd.append(sectionsV[auxIndex])
		
	strOrd = ''.join(sectionsOrd)
	res = [strOrd[i::auxCount] for i in range(auxCount)]
	return ''.join(res)
	
def main():
	"""Función principal main

	Esta función tiene dos opciones: cifrar o descifrar. Se le pregunta al usuario que
	proceso desea realizar. En ambos casos se pide el mensaje y la clave con que se van
	a utilizar en el proceso y se muestra en pantalla el resulatdo de la operación realizada 
	"""
	print("******** CODIFICADOR ********")
	print("\nMENU:\n1. Cifrar mensaje\n2. Descifrar mensaje")
	opcion = int(input("Escriba su opcion: "))

	print("\nEscriba el mensaje")
	mensaje = input()
	print("\nEscriba la clave")
	key = input()
	
	if opcion == 1:
		print("\nMensaje cifrado:\n")
		print(cryptographer(mensaje, key))
	else:
		print("\nMensaje descifrado:\n")
		print(decipher(mensaje, key))

main()