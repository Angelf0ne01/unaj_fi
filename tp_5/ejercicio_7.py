# Ejercicio 7: Escriba un programa que lea números de documentos de identidad de
# personas hasta que se ingrese el número “999”. Debe imprimir la cantidad de números de
# documentos menores que 20.000.000.


numeros = []
cantidad = 0

numero = input("Ingrese número de documento: ")
while numero != "999":
    numero = input("Ingrese número de documento: ")
    numeros.append(int(numero))



for numero in numeros:
    if numero < 20000000:
        cantidad = cantidad + 1

print("Cantidad de números de documentos menores que 20.000.000: ", cantidad)
