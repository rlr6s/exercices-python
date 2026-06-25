'''Escribir un programa que pida al usuario que introduzca una 
frase en la consola y muestre por pantalla la frase invertida.'''

def main():
    frase = input("ingrese una frase: ")
    
    frase_invertida = frase[::-1]
    
    print(f"frase invertida:{frase_invertida}")
    
    
main()