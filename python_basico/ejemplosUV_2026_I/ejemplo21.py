# funcion hipotenusa
import math
def calcularHipotenusa(cateto1,cateto2):
	h=math.sqrt( math.pow(cateto1,2) + math.pow(cateto2,2))
	return h

a=int(input("Ingrese el primer cateto:"))
b=int(input("Ingrese el segundo cateto:"))

h=calcularHipotenusa(a,b)

print("La hipotenusa: ",h)
## llamamos a pi, porque sí!
print(math.pi)
h=0
print("h es...",h)
