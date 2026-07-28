nombres_est =[None]*4
print ("Nombres=",nombres_est )

notas =[None]*3
print("Notas=", notas)

edades = [None]*3
print("Edades=",edades)

nombres_est[0]="Juan"
print("Nombres=", nombres_est)
nombres_est[1]="Sarah"
print("Nombres=",nombres_est)
nombres_est[2]="Oscar"
print("Nombres=",nombres_est)
nombres_est[3]="Maria"
print("Nombres=",nombres_est)

nombre_anterior=nombres_est[2] #guardar dato que voy a sobreescribir
nombres_est[2]="Juana"
print("Nombres=", nombres_est)
print("Estudiante canceló: "+nombre_anterior)

print("Estudiante 2°=", nombres_est[2])

notas[0]=2.7
notas[1]=3.1
notas[2]=2.5
print("nota 1°=",notas[1])
print(type(notas))
suma_notas= notas[0]+notas[1]
print("Suma de notas es: ",round(suma_notas,1))
## arreglo de 100 números
numeros=[None]*100
for i in range(10):
	numeros[i]=int(input("Ingrese un valor: "))

for i in range(100):
	print(numeros[i])

for i in range(10):
	if(numeros[i]%2==0):
		print(numeros[i]) ## solo muestra los numeros pares
s=0
for i in range(100):#progesion aritmetica
	s= s + (i*i)
print(s)
suma=0
for i in range(10):
	suma= suma + numeros[i]
print(suma)

