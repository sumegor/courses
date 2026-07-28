# Tienda de alquiler de peliculas
cantidad_peliculas=int(input("Ingrese la cantidad de películas: "))
datos_peliculas="" #inicializar la variable de tipo string

for n in range(0, cantidad_peliculas):
	print("------------------------")
	print("\tPelícula #"+str(n+1))
	print("------------------------")
	formato_peli=input("Ingrese el formato (DVD o VHS) de la película: ")
	genero_peli=input("Ingrese el género (comedia, acción, drama) de la película: ")
	datos_peliculas= datos_peliculas+ "-->\tPelícula #"+str(n+1)+" : "+formato_peli +"|" + genero_peli+"\n"
	#datos_peliculas+= formato_peli +"|" + genero_peli+"\n"

print("Resumen\n"+datos_peliculas)
# w: write
# x: crear
# r: read
## C:\Users\sumeg\OneDrive\Documentos\univalle\Informatica_I
ruta="C:\\Users\\sumeg\\OneDrive\\Documentos\\univalle\\Informatica_I\\Ejemplos\\"
#No funcion con tildes  # ruta="C:/Users/sumeg/OneDrive/Documentos/univalle/Informática_I/Ejemplos/"

with open(str(ruta)+"datos_peliculas.txt","w", encoding="utf-8") as archivo:
	archivo.write(datos_peliculas)

print("archivo guardado!")
