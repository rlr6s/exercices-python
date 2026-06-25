'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''

def main ():
    palabra = input("ingrese un palindromo: ").strip()
    print(es_palindromo(palabra))
    
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    
    return palabra == palabra[::-1]
    
main()