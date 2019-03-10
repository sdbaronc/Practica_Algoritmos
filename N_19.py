import math

print("Algoritmo que imprima cordenadas en un plano")

x1=int(input("Digita un numero: "))
y1=int(input("Digita un numero de nuevo: "))
x2=int(input("Digita un numero de nuevo x2: "))
y2=int(input("Digita un numero de nuevo x3: "))

d=math.sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))

print("La distancia entre las cordenadas (x1,y1) y (x2,y2) es " + str(d))
print("Final del programa")

# numero 19