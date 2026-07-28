# Tienda de alquiler de peliculas organizado en funciones 
# Solo funciones
#
#global datos_peliculas #inicializar la variable de tipo string

def bienvenida(datos_peliculas):
	cantidad_peliculas=int(input("Ingrese la cantidad de películas: "))
	#datos_peliculas="" ## string sin nada
	return cantidad_peliculas

def ingresar_peliculas(cantidad_peliculas,datos_peliculas):
	lista_nombres_pelis =[None]*cantidad_peliculas

	for n in range(0, cantidad_peliculas):
		print("------------------------")
		print("\tPelícula #"+str(n+1))
		print("------------------------")
		nombres_pelis=input("Ingrese el nombre de la película: ")
		lista_nombres_pelis[n]=nombres_pelis
		calificacion_imbd=float(input("Ingrese la calificación de la película: "))
		formato_peli=input("Ingrese el formato (DVD o VHS) de la película: ")
		genero_peli=input("Ingrese el género (comedia, acción, drama) de la película: ")

		datos_peliculas= datos_peliculas+ "-->\tPelícula #"+str(n+1)+" : "+nombres_pelis+"|"+str(calificacion_imbd)+"|"+formato_peli +"|" + genero_peli+"\n"
		#datos_peliculas+= formato_peli +"|" + genero_peli+"\n"
	print("Resumen\n"+datos_peliculas)
	return datos_peliculas


def guardar_archivo(datos_peliculas,ruta,nombre_archivo="datos_peliculas_jun22.txt"):
	# Tipos de manejo de archivos
	# w: write
	# x: crear
	# r: read
	## C:\Users\sumeg\OneDrive\Documentos\univalle\Informatica_I
	### ruta="C:\\Users\\sumeg\\OneDrive\\Documentos\\univalle\\Informatica_I\\Ejemplos\\"
	#No funcion con tildes  # ruta="C:/Users/sumeg/OneDrive/Documentos/univalle/Informática_I/Ejemplos/"

	with open(str(ruta)+nombre_archivo,"w", encoding="utf-8") as archivo:
		archivo.write(datos_peliculas)

	print("archivo guardado!")


## Llamando las funciones para mi Tienda de peliculas
def iniciando_Tienda():
	datos_peliculas=""

	num_peliculas=bienvenida(datos_peliculas)
	datos_peliculas=ingresar_peliculas(num_peliculas,datos_peliculas) 
	ruta="C:\\Users\\sumeg\\OneDrive\\Documentos\\univalle\\Informatica_I\\Ejemplos\\"
	guardar_archivo(datos_peliculas,ruta)

iniciando_Tienda()
