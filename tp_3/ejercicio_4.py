'''
Autor: Angel Vazquez
Comision: 17
Ejercicio 4: Definir una función denominada “imprimo_fecha” que reciba tres cadenas de caracteres que representan un día, un mes y un año e imprima  la fecha de la siguiente manera: “ 21 de septiembre de 2012”.

'''


def imprimo_fecha(dd, mm, yyyy):
    fecha = str(dd)+" de "+str(mm)+" de "+str(yyyy)
    print(fecha)


imprimo_fecha(21, "septiembre", 2012)
imprimo_fecha(2, "enero", 2015)
imprimo_fecha(16, "diciembre", 2001)
