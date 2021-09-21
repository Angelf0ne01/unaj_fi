'''
Ejercicio 2: Defina la diferencia entre una lista y una tupla. ¿En qué casos utilizarías cada una? De ejemplos donde que requiera una o la otra.



Resp:
La diferencia entre una lista y una tupla, es que la tuplas son inmutables, mientras que las listas si.
Se puede utilizar las tuplas para definir valores que no se van a modificar en tiempo de ejecucion, ejemplo los dias de una semana. 

Ejemplo tuplas:
dias=('lunes','martes','miercoles','jueves','viernes','sabado','domingo')

En cambio una lista, puede variar su contenido. Modificar los elementos como agregar, eliminar o modificar.
'''
#Ejemplo:

lista_alumnos=[]
#agrego una nuevo alumno a la lista.
lista_alumnos.append('jose')
lista_alumnos.append('juan')
#modificar
lista_alumnos[0]='marta'
#output--> ['marta','juan']

#a su vez, tambien puedo agregar una lista adentro de una lista.
order=[]
products=['alfajor','caramelos']
order.append(products)


