print("Algoritmo que imprima los primeros numeros siguiendo secuencias indicadas")

n=int(input("Digita un numero: "))

for num in range(1,n+1):
	if num%2==0:
		num=num*-1
	print(num)

print("Final del programa")

# numero 60		
