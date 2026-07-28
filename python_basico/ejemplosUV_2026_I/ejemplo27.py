# funcion recursiva

def funcionR2(n):
	if(n==0):
		print("Se cumplió la condición base!")
		return 1
	else:
		print("Llamando a: n + funcionR2 (",n,"- 1)")
		return n + funcionR2(n-1) # si lo cmabias a n - 2 y llamas a n con número impar hay error de recursión!

resultado=funcionR2(3)
print(resultado)