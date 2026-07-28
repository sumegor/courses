
# funcion recursiva

def funcionR1(n):
	if(n==0):
		print("Se cumplió la condición base!")
		return 1
	else:
		print("Llamando a: n * funcionR1 (",n,"- 1)")
		return n*funcionR1(n-1)

resultado=funcionR1(3)
print(resultado)







