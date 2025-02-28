'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''


def main():
    cadena = input("Ingrese una cadena: ")
    cadena_inversa = inversa(cadena)
    if es_palindromo(cadena):
        print("Es palindromo")
    else:
        print("No es palindromo")
def inversa(cadena):
    
    return cadena[::-1] 

def es_palindromo(cadena):
    return cadena == inversa(cadena)   

  
main()
