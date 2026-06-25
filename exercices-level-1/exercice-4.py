'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''

def main():
    X = input("ingrese un caracter:")
    print(vocal(X))
    
def vocal(char):
    if char in 'aeiouAEIOU':
        return True
    else:
        return False
    
main()