'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''

def main():
    cadena = input("ingrese una cadena: ")
    print(inversa(cadena))
    
def inversa(cadena):
    cadena_inversa = cadena[::-1]
    return cadena_inversa 

main()
                                
    