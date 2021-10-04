'''
Autor: Angel Vazquez
Comision: 17
Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números. Uno para la cantidad de días que debe suministrarse el remedio, el segundo dato para la cantidad de veces por día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza.
'''


def calculo_dosis(dosis, dias, comprimidos):
    calculo = (dias*dosis)/comprimidos
    return int(calculo)==0
    


print(calculo_dosis(50,5,1000)) #alcanza
print(calculo_dosis(50,500,1000)) #no alcanza
