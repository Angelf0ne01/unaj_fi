#Ejercicio 12: Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67 ] escribir un
#programa que muestre el número más alto.


lista = [1, 14, 56, 43, 23, 46, 58, 123, 67]

mayor = 0

for i in lista:
    if i > mayor:
        mayor = i

print("El número más alto es:", mayor)
