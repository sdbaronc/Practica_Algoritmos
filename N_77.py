print("Algoritmo que imprima un usuario y contraseña definidos")

usuario=input("Digita tu usuario: ")
contraseña=int(input("Digita tu contraseña: "))
intentos=0

while usuario!="henry" and contraseña!=1234:
	if intentos==2:
		print("Has consumido demaciados intentos, El programa ha finalizado")
		break
	usuario=input("Digita tu usuario: ")
	contraseña=int(input("Digita tu contraseña: "))
	intentos+=1

if usuario=="henry" and contraseña==1234:
	print("Usuario y contraseña digitados correctamente")

print("Final del programa")

# numero 77