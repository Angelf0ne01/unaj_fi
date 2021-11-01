#Ejercicio 13: Escriba un programa que solicite nombres de localidades y códigos postales
#al usuario hasta que se ingresa el código postal 0. Debe generar una lista con todos los
#valores ingresados e imprimirla.


lista_localidades = []


codigo_postal = int(input('Ingrese codigo postal: '))

while codigo_postal != 0:
    localidad = input('Ingrese localidad: ')
    lista_localidades.append([localidad, codigo_postal])    
    codigo_postal = int(input('Ingrese codigo postal: '))

for i in lista_localidades:
    print(i)