print("Algoritmo que imprima cuantos numeros mayores y menores que 100 hay")

mayor=0
menor=0
igual=0

n=int(input("Digita un numero: "))
m=int(input("Digita un numero: "))

for num in range(n,m+1):
	if num>100:
		mayor+=1
	elif num==100:
		igual+=1
	else:
		menor+=1
print("Hay " + str(mayor) + " numeros mayores que 100")		
print("Hay " + str(menor) + " numeros menores que 100")					
print("Hay " + str(igual) + " numeros iguales que 100")
print("Final del programa")

# numero 67