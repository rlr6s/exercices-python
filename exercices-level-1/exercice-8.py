'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado. '''


import random
def main():
    lista1 = [random.randint(1,10) for _ in range (5)]
    lista2 = [random.randint(1,10) for _ in range (5)]
    
    print("lista 1", lista1)
    print("lista 2", lista2)
    print("hay superposicion?", superposicion(lista1, lista2))

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

main()