#Tratare de Encriptar un Archivo
#es el mismo metodo de encriptacion pero le agregue la funcionalidad de correr con archivos 
#se recomiendo sacar la validacion de la existencia de los archivos txt aparte 
#para que sean verificado su existencia
def EncriptarArchivo(clave):
	nombre_entrada 	= input("nombre del archivo: ") #nombre del archivo
	nombre_salida 	= input("como lo llamara al salir: ")#nombre que se utilizara para la salida
	f_entrada = open(nombre_entrada, 'r')# lo abre el archivo
	f_salida = open(nombre_salida, 'w') # comienza a escribir
	for linea in f_entrada: # comienza el encriptamiendo 
		traduccion = ''
		ClaveUsar  = clave
		for letra in linea: #proceso 
			if letra.isalpha():
				valorASCII = ord(letra)
				valorASCII += ClaveUsar
				if letra.isupper():
					if valorASCII > ord('Z'):
						valorASCII -= 26
					elif valorASCII < ord("A"):
						alorASCII+=26
				elif letra.islower():
					if valorASCII > ord('z'):
						valorASCII-=26
					elif valorASCII < ord('a'):
						valorASCII +=26
				traduccion += chr(valorASCII)
			else:
				traduccion += letra
		f_salida.write(traduccion)# va escribiendo en el archivo
	f_entrada.close() # cierra el archivo de entrada
	f_salida.close() #cierra el archivo de salida