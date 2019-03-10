print("Algoritmo que imprima la suma de dos numeros y determine si son mayor o menos que otro")

num1=int(input("Digita un numero: "))
print(num1)
num2=int(input("Digita otro numero: "))
print(num2)
num3=int(input("Digita otro numero x2: "))
print(num3)

suma=num1+num2

if suma>num3:
	print("La suma es " + str(suma))
	print("La suma del primer y segundo numero es mayor que " + str(num3))
	

elif suma==num3:
	print("La suma es " + str(suma))
	print("La suma del primer y segundo numero es igual que " + str(num3))

else:
	print("La suma es " + str(suma))
	print("La suma del primer y segundo numero es menor que " + str(num3))

print("Final del programa")

# numero 36