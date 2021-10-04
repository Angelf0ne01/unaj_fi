'''
Autor: Angel Vazquez
Comision: 17
Ejercicio 5: Definir una función denominada cuantos_dias que reciba el número de mes como parámetro y retorne la cantidad de días que posee.
Ejemplo: cuantos_dias(1), debería retornar 31. Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31], [“febrero”, 28], ...]        
'''
# constante
DIA = 1
# lista de datos
meses_max_dias = [
    ["enero", 31],
    ["febrero", 28],
    ["marzo", 31],
    ["abril", 30],
    ["mayo", 31],
    ["junio", 30],
    ["julio", 31],
    ["agosto", 31],
    ["septiembre", 30],
    ["octubre", 31],
    ["noviembre", 30],
    ["diciembre", 31],
]
# funcion


def cuantos_dias(mes):
    if(mes > 0 and mes <= 12):
        return meses_max_dias[mes-1][DIA]
print(cuantos_dias(2))
print(cuantos_dias(9))
print(cuantos_dias(12))