print("Algoritmo que imprima si un numero es positivo o negativo")

numb=int(input("Digita un numero, Por favor: "))

if numb>0:
	print("El numero " + str(numb) + " es positivo")
elif numb==0:
	print("El numero " + str(numb) + " es neutro")
else:
	print("El numero " + str(numb) + " es negativo")

print("Final del programa")
