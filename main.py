#aqui vemos ya un poco mas completa esta aplicacion que permite encriptar, y desencriptar
#mensajes por medio del cifrado cesar, tambien permite encriptar y desencriptar el contenido 
#de archivos txt.... estamos actualmente en el main 
#que simplemente contiene un while que mantiene a el scripts en ejucatamiento hasta que el usuario
#lo decida, importo la funcion PararONO que es la que se encarga de decidir cuando parar y cuando no 
#y luego lo valido. en la carpeta PACKAGE estan todos los modulos por separadados encargados de hacer esta tarea
#y los uni en un modulo llamado main, que esta dentro de todos los paquetes, que se encarga de administrar 
#los llamados de cada cosa segun el usuario lo escoja... 
import os
from package.PararONo import PararONo #metodo que decide cuando parar 
from package.main import main #ciencia del programa que es donde ordeno todo

while True:
	main() # ejecuto por lo menos una vez el meno
	run = PararONo() # luego de ejecutarse una vez , le pregunta al usuario si quiere seguir o no
	if run==1: # si la respuesta es si, sale del programa
		os.system('cls')
		break
	else: # si responde no, se ejecuta de nuevo la funcion main
		main()

