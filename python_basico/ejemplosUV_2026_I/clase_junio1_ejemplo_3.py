import numpy

#declaracion de la matriz
matriz1=numpy.zeros((20,10))## rellena la matriz con ceros de tipo float --> decimal


for i in range(0,20,1): # filas
	for j in range(0,10,1):# columnas
		#instruccion!
		matriz1[i][j]=5.0

print("matriz1--> ",matriz1)# mostrar toda la matriz1

for i in range(0,20,1): # filas
	for j in range(0,10,1):# columnas
		#instruccion!
		print(matriz1[i][j])


matriz2=numpy.zeros((3,3))## declaracion e inicializacion de datos

for i in range(0,3,1):
	for j in range(0,3,1):
		## instrucción
		matriz2[i][j]=3.0 # insertar datos en la matriz


for i in range(0,3,1): # filas
	for j in range(0,3,1):# columnas
		#instruccion!
		# mostrar toda la matriz2 y sus posiciones i,j
		print("matriz2","[",i,"]","[",j,"]","->",matriz2[i][j]) 


## mostrar datos de la primera fila de la matriz1
## opción 1
print(matriz1[0])

## opción 2: + control
print("datos de la primera fila de la matriz1 (i=0)")
for i in range(0,20,1): # filas
	for j in range(0,10,1):# columnas
		#instruccion!
		if(i==0):
			print(matriz1[i][j])

## mostrar datos de la primera columna de la matriz1

print("datos de la primera columna de la matriz1 (j=0)")
for i in range(0,20,1): # filas
	for j in range(0,10,1):# columnas
		#instruccion!
		#print("matriz1","[",i,"]","[",j,"]","->") 
		if(j==0):
			print(matriz1[i][j])


print("matriz--->",matriz1.shape)


##diagonal principal de la matriz
print("Diagonal de la matriz2")
for i in range(0,3,1):
	for j in range(0,3,1):
		## instrucción
		if(i==j):## si i y j son iguales es una posición de la diagonal!
			print(matriz2[i][j])

suma=0.0
## suma de todos los valores de la matriz2
for i in range(0,3,1):
	for j in range(0,3,1):
		## instrucción: suma
		suma=suma+matriz2[i][j]

print("suma de valores de matriz2-->",suma)


