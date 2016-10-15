#a continuacion se desarrollara un programa que pueda cumplir la funcion 
#de encriptar, y desencriptar textos.
#utilizando el metodo cesar
#Modulo Main donde esta definida la estructura del programa
import os 
from package.encriptar 		import encriptar
from package.desencriptar 	import desencriptar
from package.mensaje 		import mensaje
from package.menu			import menu
from package.clave 			import clave
from package.EncriptarArchivo import EncriptarArchivo
from package.DesencriptarArchivo import DesencriptarArchivo
from package.PararONo import PararONo
os.system("cls")

def main(): #metodo encargado de administrar la ejucion de cada scripts por separado
	opc = menu() # opc = menu, en el modulo menu valido que la opcion del usuario sea valida y el valor se lo doy a opc
	if opc == 1:
		os.system('cls')
		print("ENCRIPTAR TEXTO PLANO \n")
		print('\nSu texto encriptado es: \n \n' + encriptar(mensaje('encriptar'), clave()))
		print('\n'+'\n'+'\n'+'\n'+'\n'+'\n')
		os.system('pause')
	elif opc == 2:
		os.system('cls')
		print("DESENCRIPTAR TEXTO PLANO \n")
		print('\nSu texto desencriptado es: \n \n' + desencriptar(mensaje('desencriptar'), clave()))
		print('\n'+'\n'+'\n'+'\n'+'\n'+'\n')
		os.system('pause')
	elif opc == 3:
		os.system('cls')
		print("ENCRIPTAR ARCHIVO \n")
		EncriptarArchivo(clave())
		os.system('cls')
		print("COMPLETADO")
		print('\n'+'\n'+'\n'+'\n'+'\n'+'\n')
		os.system('pause')
	elif opc==4:
		os.system('cls')
		print("DESENCRIPTAR ARCHIVO \n")
		DesencriptarArchivo(clave())
		os.system('cls')
		print("COMPLETADO")
		print('\n'+'\n'+'\n'+'\n'+'\n'+'\n')
		os.system('pause')
	elif opc==5: 
		os.system('exit')