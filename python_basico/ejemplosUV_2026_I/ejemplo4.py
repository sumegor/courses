#Calcula IVA de una venta


venta = int(input("Digite el valor de la venta:"))

iva= venta * 0.16

print("El IVA de la venta es: ", iva)

total= venta + iva
print("El valor total de venta (IVA incluido) es: ",total)
print(type(total))
