print("Algoritmo que invierta numeros")

a=int(input("Digita el numero de 4 cifras que deseas invertir: ")) #3245

b=int(a/1000) #3
c=a-(b*1000) #245
d=int(c/100) #2
e=c-(d*100) #45
f=int(e/10) #4
g=e-(f*10) #5

print(str(g) + str(f) + str(d) + str(b))

# numero 25