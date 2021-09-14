'''
    Autor:Angel Vazquez
    Comision: 17
    
    Ejercicio 18: Pedir nombre, apellido de una persona y el día, mes, año en que nació. Armarle una
    clave con esos datos (su clave seria sus iniciales seguido de un guión bajo y de su año de
    nacimiento) y mostrarla
'''
# obtengo los datos del usuario
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
fecha_de_nacimiento = str(input("Ingrese su fecha de nacimiento: "))
# creo la contraseña nueva
password = nombre[0]+apellido[0]+"_"+fecha_de_nacimiento[-4:]
# muestro por consola, la nueva contraseña del usuario.
print("la contraseña es: ", password)
