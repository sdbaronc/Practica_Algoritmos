import math
print("Algoritmo que imprima el area de un hexagono")

lado_hex=float(input("Digita un lado del hexagono en cm: "))

apotema=math.sqrt(lado_hex*lado_hex-((lado_hex*lado_hex)/(2*2)))
perimetro=6*lado_hex
area=(perimetro*apotema)/2

print("El area del hexagono es " + str(area))
print("Final del programa")

