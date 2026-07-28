## Recibir dos números y determinar cuál es mayor

numero1=int(input("Digite el primer número: "))
numero2=int(input("Digite el segundo número: "))


if(numero1>numero2):
	print(numero1," es mayor que ", numero2)
elif(numero2>numero1):
	print(numero2," es mayor que ", numero1)
else:
	### condicion ---> if (numero1 == numero2)
	print("Los números son iguales!")