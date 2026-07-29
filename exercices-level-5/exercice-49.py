'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no. '''


num = int(input("ingrese un numero primo: "))

if not num % 1 == 0 and num % num == 0:
    print("no es un numero primo")
else:
    print("es primo")