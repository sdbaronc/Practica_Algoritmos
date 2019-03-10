print("Algoritmo que determine el iva de una venta")

venta=float(input("Digita el valor del producto que deseas comprar: "))

iva=venta*0.19
venta_total=int(venta+iva)
descuento=venta*0.05
venta_descuento=int(venta-descuento)

if venta<150000:
	print("El precio a pagar es de " + str(venta_total))
else:
	print("El precio a pagar con un descuento del 5 porciento es " + str(venta_descuento))

print("Final del programa")

# numero 30