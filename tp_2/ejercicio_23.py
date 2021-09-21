'''
    Autor: Angel Vazquez
    Comision:17 
    
    Ejercicio 23: Dada la siguiente información, elija una estructura de datos que permita guardarla
    adecuadamente
    ● Guerra del Peloponeso 431 a.C
    ● Revolución de Mayo 1810 d.C
    ● Llegada de los españoles a América 1492 d.C
    ● Comienzo de la construcción de la gran Muralla China 214 a.C
'''

# sub-indices de siglos.
AC = 0
DC = 1

# creo una tapa con los siglos: Antes de cristo (A.C) y Despues de Cristo (D.C).
siglo = ("a.c", "d.c")
# en esta lista, voy a guardar todos los acontecimientos.
lista_de_acontecimiento = []
# acontecimientos
acontecimiento_1 = []
acontecimiento_2 = []
acontecimiento_3 = []
acontecimiento_4 = []
# agrego la informacion sobre el acontecimiento 1.
acontecimiento_1.append("Guerra del Peloponeso")
acontecimiento_1.append(431)
acontecimiento_1.append(siglo[AC])
# agrego la informacion sobre el acontecimiento 2.
acontecimiento_2.append("Revolución de Mayo")
acontecimiento_2.append(1080)
acontecimiento_2.append(siglo[DC])
# agrego la informacion sobre el acontecimiento 3.
acontecimiento_3.append("Llegada de los españoles a América")
acontecimiento_3.append(1492)
acontecimiento_3.append(siglo[DC])
# agrego la informacion sobre el acontecimiento 4.
acontecimiento_4.append("Comienzo de la construcción de la gran Muralla China")
acontecimiento_4.append(214)
acontecimiento_4.append(siglo[AC])


lista_de_acontecimiento.append(acontecimiento_1)
lista_de_acontecimiento.append(acontecimiento_2)
lista_de_acontecimiento.append(acontecimiento_3)
lista_de_acontecimiento.append(acontecimiento_4)

# print(lista_de_acontecimiento)
for acontecimiento in lista_de_acontecimiento :
    #cambio todo los tipos de datos a un string.
    acontecimiento_serialize=map(str,acontecimiento)
    #imprimo la lista utilizando el join para unir los elementos del arreglo y separandolos por un espacio.
    print(' '.join(acontecimiento_serialize))

