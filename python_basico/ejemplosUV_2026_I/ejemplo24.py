# funcion sin entradas
def funcion():

	z=0 # z es del universo local!
	print(z)

z=10 # z es del universo global!

print(z) # esta es la global!

funcion() # AQUI z es la local! 
print(z) # SIGUE z global!

def funcion_cambia(a):
	z=a # z es local
	return z # z va para otro universo...

#z=100 # z es global
#z=funcion_cambia(1)
#print(z) # z es global

