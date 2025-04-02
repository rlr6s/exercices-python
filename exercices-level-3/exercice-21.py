'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como 
el número introducido.'''

def main():
    nombres = input("Ingrese su nombre: ")
    n = int(input("Ingrese un número entero: "))

    for _ in range(n):
        print(nombres)
main()
