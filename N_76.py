print("Algoritmo que imprima los factores de un numero")

cont=0
a=int(input("Digita un numero: "))

for i in range(1,a+1):
	if a%i==0:
		cont+=1
		
print(cont)
print("Final del programa")		

# numero 76