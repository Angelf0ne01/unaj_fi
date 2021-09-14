'''
Autor: Angel Vazquez
Comision: 17


Ejercicio 21: Dada la siguiente estructura: lista=[1,True,['a','b','c'], "hola"]. Ejecutar la siguientes
sentencias y describir los resultados.
a) print (lista[2])
b) print (lista [4])
c) lista.append (False)
print (lista)
'''

lista = [1, True, ['a', 'b', 'c'], "hola"]
#imprimo el elemento del sub-indice 2
print(lista[2])
#imprimo el elemento del sub-indice 3
print(lista[3])
#agrego un nuevo elemento a la lista.
lista.append(False)
#imprimo todos los elemento de la lista
print(lista)
