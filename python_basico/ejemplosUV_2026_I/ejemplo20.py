# funcion Misterio #2

def funcionMisterio(a,b):
	if( (a+b)<5 or (a+b)>10):
		misterio= 2*a+b
	else:
		misterio=b*b-a*3
	return misterio

misterio=funcionMisterio(5,8)
print("El valor de la funcion Misterio es: ", misterio) 

misterio=funcionMisterio(3,2)
print("El valor de la funcion Misterio es: ", misterio) 
