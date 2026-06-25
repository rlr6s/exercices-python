'''Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".'''

def main():
    caracter = input("ingrese un caracter: ")
    n = int(input("cuantas veces quiere repetir este caracter: "))
    print(generar_n_caracteres(caracter, n))
    
def generar_n_caracteres(caracter, n):
    
    return caracter * n


main()
    
