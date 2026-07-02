'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.'''

def main():
    num = int(input("ingrese un numero: "))
    if num % 2 == 0:
        print("even")

    else:
        print("odd")

main()