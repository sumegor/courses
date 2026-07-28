import numpy

Numeros=numpy.zeros((2,3)) #2 filas, 3 columnas

Numeros[1][1]=2
Numeros[1][0]=4
Numeros[1][2]=6
Numeros[0][1]=7
Numeros[0][2]=1

calculo1=(Numeros[0][1]*Numeros[0][2]) - Numeros[1][2]
calculo2=Numeros[1][1] + (Numeros[1][0]/2) - (Numeros[0][0]*4)
calculo3= (4*Numeros[1][2]) - (10*Numeros[1][0])

print("Valor1 ",calculo1)
print("Valor2 ", calculo2)
print("Valor3 ", calculo3)
print("tipo dato --> Numeros[1][1] ", type(Numeros[1][1]))
print("tipo dato --> calculo1 ", type(calculo1))








