print("Algoritmo que imprima dada cantidad de segundos en tiempo real")

segundos=int(input("Digita la cantidad de segundos: "))

minutos=segundos/60
segundos_2=int(segundos%60)
horas=int(minutos/60)
minutos_2=int(minutos%60)

print("Tiempo " + str(horas) + ":" + str(minutos_2) + ":" + str(segundos_2))
print("Final del programa")

# numero 23