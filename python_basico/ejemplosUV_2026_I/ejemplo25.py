# funcion - ejemplo comprar ropa
#inputs (entradas): 
def comprar_ropa(nombre, talla, color):
	if(color=="blanco"):
		#lo q sucede si color es blanco
		precio=20000
	elif(color=="negro"):
		precio=50000
	elif(color=="azul"):
		precio=10000
	elif(color=="verde"):
		precio=12000
	elif(color=="amarillo"):
		precio=8000
	elif(color=="rojo"):
		precio=9000
	elif(color=="fucsia"):
		precio=5000
	elif(color=="morado"):
		precio=9500
	else:
		precio=0
		mensaje="Este color no está disponible en este momento!"
		print(mensaje)

	return precio

nombre_ropa=input("Ingrese el tipo de ropa/prenda: ")
talla_ropa=input("Ingrese la talla: ")
color_ropa=input("Ingrese el color: ")
precio= comprar_ropa(nombre_ropa, talla_ropa, color_ropa)

print("--------------------------------------------")
print("La prenda seleccionada fue: ",nombre_ropa)
print("La talla seleccionada fue: ",talla_ropa)
print("El color seleccionado fue: ",color_ropa)
print("El precio a pagar es: ",precio)
print("--------------------------------------------")

