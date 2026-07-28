import numpy

##calcular el promedio de datos de cada fila d ela sgte matriz:


matriz33=numpy.zeros((3,3))
## relleno manual de cada posicion de la matriz33
matriz33[0][0]=2
matriz33[0][1]=3
matriz33[0][2]=1
matriz33[1][0]=4
matriz33[1][1]=0
matriz33[1][2]=5
matriz33[2][0]=1
matriz33[2][1]=1
matriz33[2][2]=6

#inicializar variables contadores y acumuladores
valor_fila=0.0
promedio=0.0
for i in range(0,3,1):
	print("fila-->",i)
	for j in range(0,3,1):
		valor_fila=valor_fila+matriz33[i][j]
		promedio=valor_fila/3
	print("suma por fila->", valor_fila)
	print("promedio por fila",i,"->",promedio)
	valor_fila=0.0




