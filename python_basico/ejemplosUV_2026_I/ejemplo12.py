## RANGOS DE EDADES
## menores de edad, adultos y tercera edad

edad= int( input("Ingrese la edad: "))

if(edad>0 and edad<18):
	print("Es menor de edad")
elif(edad>=18 and edad<60):
	print("Es un adulto")
elif(edad>=60 and edad<100):
	print("Es de la tercera edad")
elif(edad>=100 and edad<150):
	print("Es centenario! o_o ")
else:
	print("Edad no válida!")
