#Ejercicio 1: Escribir un programa que muestre la tabla de multiplicar de un número
#introducido por teclado por el usuario.


tabla = int(input("Introduce la tabla de multiplicar que quieres ver: "))

for i in range(1,11):
    print(tabla, "x", i, "=", tabla*i)