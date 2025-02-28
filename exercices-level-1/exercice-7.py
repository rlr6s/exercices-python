'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''


def main():
    palabra = input("ingrese una palabra: ")
    print(palindromo(palabra))

def palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False
    

main()
