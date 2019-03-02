print("Algoritmo que imprima que dada cantidad de segundos indique cuantas horas representa")

segundos=int(input("Digita la cantidad de segundos que deseas convertir a horas: "))

minutos=segundos/60
hora=minutos/60

print("En " + str(segundos) + " segundos hay " + str(hora) + " horas")
print("Final del programa")
