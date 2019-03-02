print("Algoritmo que imprima la velocidad final de un objeto")

t=float(input("Digita el tiempo en segundos: "))
a=float(input("Digita la aceleracion en m/s^2: "))
v_inicial=float(input("Digita la velocidad inicial en m/s: "))

V_final=(a*t)+v_inicial

print("La velocidad final es de " + str(V_final) + "m/s")
print("Final del programa")
