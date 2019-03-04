print("Algoritmo que imprima si un numero es par (positivo,negativo) o impar (positivo,negativo)")

numb=int(input("Digita un numero, Por favor: "))

if numb>0:
	if numb%2==0:
		print("El numero " + str(numb) + " es par positivo")
	else:
		print("El numero " + str(numb) + " es impar positivo")
else:
	if numb%2==0:
		print("El numero " + str(numb) + " es par negativo")
	else:
		print("El numero " + str(numb) + " es impar negativo")

print("Final del programa")

		