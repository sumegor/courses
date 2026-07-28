
#Venta de películas
cantidad_peli=int( input(" Por favor ingrese la cantidad de películas Blu-ray: ") )

valor_peli_blu_ray = 65000

total_pagar= valor_peli_blu_ray * cantidad_peli

iva_peli= total_pagar * 0.16

ganancia_neta= total_pagar - iva_peli
print("-"*15)
print("DATOS VENTA")
print("-"*15)
print("Total a pagar: ","$ ", total_pagar)
print("IVA: ","$ ", iva_peli)
print("Ganancia neta: ","$ ",ganancia_neta)
print("--------------------------------")
print("Vuelve pronto!")
