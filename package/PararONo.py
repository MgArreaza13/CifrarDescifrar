#metodo decide si parar o no la ejucion del script
import os 
def PararONo():
	rpd = 0
	while True:
		os.system('cls')
		rpd = int(input('DESEA PARAR LA EJECUCION DEL PROGRAMA\n 1)SI\n 2)NO\n'))
		if rpd>=1 and rpd<=2:
			return rpd