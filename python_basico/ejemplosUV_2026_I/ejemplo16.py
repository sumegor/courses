#funciones

# entradas
# a: número real
# b: número real

# salidas
# f(a,b): número real

# definición función
def funcion_cuadratica_ab ( numeroA, numeroB ):

	f_ab=3*numeroA*numeroA +2*numeroA*numeroB -7

	return f_ab

r1=funcion_cuadratica_ab(3,-1)
r2=funcion_cuadratica_ab(-7,0)
r3=funcion_cuadratica_ab(6,2)

print("El resultado de f(3,-1) = ",r1)
print("El resultado de f(3,-1) = ",funcion_cuadratica_ab(3,-1))

print("El resultado de f(-7,0) = ",r2)
print("El resultado de f(6,2) = ",r3)


