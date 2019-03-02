print("Algoritmo que determine la menor cantidad de billetes de cada denominacion")

dinero=int(input("Digita la cantidad de dinero: "))

mil50=int(dinero/50000)
mil20=int(dinero/20000)
mil10=int(dinero/10000)
mil5=int(dinero/5000)
mil2=int(dinero/2000)
mil1=int(dinero/1000)

print("Billetes de 50 mil serian " + str(mil50))
print("Billetes de 20 mil serian " + str(mil20))
print("Billetes de 10 mil serian " + str(mil10))
print("Billetes de 5 mil serian " + str(mil5))
print("Billetes de 2 mil serian " + str(mil2))
print("Billetes de 1 mil serian " + str(mil1))
print("Final del programa")