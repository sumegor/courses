# area y perímetro de rectangulo
def calcular_area(base, altura):
	area= base*altura
	return area 

def calcular_perimetro(base, altura):
	perimetro=2*base + 2*altura
	return  perimetro

area1=calcular_area(6.5,7.1)
perimetro1=calcular_perimetro(6.5, 7.1)
print("Area: ", area1, " Perimetro: ", perimetro1)

area2=calcular_area(8.1,4.4)
perimetro2=calcular_perimetro(8.1,4.4)
print("Area: ", area2, " Perimetro: ", perimetro2)
