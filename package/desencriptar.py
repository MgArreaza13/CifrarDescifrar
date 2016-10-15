#desarrollo del metodo que desencripta algun texto
def desencriptar(mensaje, clave):
	ClaveUsar  = -clave
	traduccion = ''
	for letra in mensaje:
		if letra.isalpha(): #verifica si es solo una palabra
			valorASCII = ord(letra) #obtengo el valor de la tabla ASCII de la letra 
			valorASCII += ClaveUsar #le sumo el valor de la clave para modificar la letra 
			if letra.isupper(): #verifica si son texto con espacios
				if valorASCII > ord('Z'): #verifica el caso especial de Z
					valorASCII -= 26
				elif valorASCII < ord("A"): #verifica el caso especial de A
					valorASCII+=26
			elif letra.islower():
				if valorASCII > ord('z'): #verifica el caso especial de z
					valorASCII-=26
				elif valorASCII < ord('a'): #verifica el caso especial de a
					valorASCII +=26
			traduccion += chr(valorASCII)
		else:
			traduccion += letra
	return traduccion