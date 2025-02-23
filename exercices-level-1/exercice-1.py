'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
muy buen ejercicio'''


def main():
    print(max())

def max():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    if a > b:
        return a
    else:
        return b
    

main()
