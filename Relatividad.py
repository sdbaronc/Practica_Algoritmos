print("Algoritmo que imprima la energia en jules de un objeto")

m=float(input("Digita la masa en kg: "))
c=float(input("Digita la velocidad de la luz en m/s: "))

energia=m*(c*c)
energia_f=energia/1000

print("La energia de un objeto es " + str(energia_f) + "jules")
print("Final del programa")

