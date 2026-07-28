## Recibir dos números y determinar cuál es mayor

numero1=int(input("Digite el primer número: "))
numero2=int(input("Digite el segundo número: "))
numero3=int(input("Digite el tercer número: "))

if(numero1>numero2  and numero1>numero3):
	print(numero1," es mayor")
elif(numero2>numero1 and numero2> numero3):
	print(numero2," es mayor")
elif(numero3>numero1 and numero3 > numero2):
	print(numero3," es mayor")
elif(numero1== numero2 and numero2==numero3):
	print("Los tres números son iguales")