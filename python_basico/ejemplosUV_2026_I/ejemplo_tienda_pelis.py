# Tienda de alquiler de peliculas
cantidad_peliculas=int(input("Ingrese la cantidad de películas: "))
#inicializar la variable de tipo string
datos_peliculas=""

for n in range(0, cantidad_peliculas):
	print("------------------------")
	print("\tPelícula #"+str(n+1))
	print("------------------------")
	formato_peli=input("Ingrese el formato (DVD o VHS) de la película: ")
	genero_peli=input("Ingrese el género (comedia, acción, drama) de la película: ")
	datos_peliculas= datos_peliculas+ "-->\t\tPelícula #"+str(n+1)+" : "+formato_peli +"|" + genero_peli+"\n\n"
	#datos_peliculas+= formato_peli +"|" + genero_peli+"\n"

print("Resumen\n"+datos_peliculas)