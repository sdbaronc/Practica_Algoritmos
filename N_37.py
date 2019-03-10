print("Algoritmo que imprima el valor de un pasaje de avion")

distancia=int(input("Digita la distancia de tu destino, Por favor: "))
n_dias=int(input("Digita la cantidad de dias que deseas quedarte, Por favor: "))

valor_distancia=distancia*5000
valor_descuento=valor_distancia*0.15
valor_viajed=int(valor_distancia-valor_descuento)

if distancia<=20:
	print("El valor de tu pasaje es de 100000")
elif distancia>=1000 and n_dias>=7:
	print("El valor de tu pasaje es de " + str(valor_viajed))
else:
	print("El valor de tu pasaje es de " + str(valor_distancia))

print("Final del programa")	

# numero 37