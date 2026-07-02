'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error. '''

def main():
    n1 = int(input("ingrese un numero: "))
    n2 = int(input("ingrese otro numero: "))

    try:
        div = n1 / n2
        print(div)
    except ZeroDivisionError:
        print("error")

main()