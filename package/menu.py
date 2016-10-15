#metodo que muestra el menu, y recoge la opcion valida que necesita ejecutar el usuario
import os
def menu(): #menu
	opc = 0
	while True:
		os.system("cls")
		print("Selecione una opcion que decea relizar \n" 
				+"\n1)Encriptar Texto Plano \n" 
				+"2)Desencriptar Texto Plano\n"
				+"3)Encriptar Archivo .TXT \n"
				+"4)Desencriptar Archivo .TXT \n"
				+"5)SALIR"
	       	)
		opc = int(input("\nSeleccione una opcion valida:  "))
		if opc>=1 and opc<=5:
			return opc
