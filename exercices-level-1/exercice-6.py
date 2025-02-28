'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''


def main():
    cadena = input("Ingrese una cadena: ")
    cadena_inversa = inversa(cadena)
    print(cadena_inversa)

def inversa(cadena):
    
    return cadena[::-1] 

     

  
main()

