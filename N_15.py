print("Algoritmo que imprima la distancia recorrida por un objeto")

t=float(input("Digita el tiempo en segundos: "))
a=float(input("Digita la acelaracion en m/s^2: "))
v=float(input("Digita la velocidad en m/s: "))

distancia=0.5*a*(t*t)+v*t

print("La distancia recorrida es " + str(distancia) + "m")
print("Final del programa")

# numero 15