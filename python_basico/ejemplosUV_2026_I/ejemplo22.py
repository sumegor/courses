# funciones: diferencia local y global

def funcion(x,y):
	z=x+y # z es local!
	print(z)

z= -5 # Esta z es global!! Es de otro universo...
funcion(5,3)

print(z) # z global!

