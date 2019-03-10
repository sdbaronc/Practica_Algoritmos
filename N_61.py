print("Algoritmo que imprima numeros naturales contenidos en n y m numeros")

n=int(input("Digita un numero: "))
m=int(input("Digita un numero: "))

if m>n:
	print("Continuar el programa")
else:
	print("Parar el programa")

for num in range(n,m+1):
	print(num)

print("Final del programa")

# numero 61	