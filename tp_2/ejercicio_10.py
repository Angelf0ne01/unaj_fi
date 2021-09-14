'''
    Autor: Angel Vazquez
    Comision: 17
    
    Ejercicio 10: Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que
    comprar (son de 60x60 cm)
'''
import math

# variables globales
largo_panel = 60
ancho_panel = 60
# obtengo el area del panel.
area_panel = largo_panel*ancho_panel

# obtengo a traves del input los datos del largo y ancho del terreno.
largo_terreno = int(input("ingrese el largo del terreno: "))
ancho_terreno = int(input("ingrese el ancho del terreno: "))
# obtengo el area del terreno.
area_terreno = largo_terreno*ancho_terreno
# obtengo la catudad de paneles a comprar
cantidad_de_paneles = area_terreno/area_panel 
# redondeo para arriba    
cantidad_de_paneles = math.ceil(cantidad_de_paneles)
# informo al usuario
print("Cantidad de paneles a comprar son: ", cantidad_de_paneles)
