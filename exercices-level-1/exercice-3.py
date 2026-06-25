'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''

def main():
    
    inpot = input("ingrese una cadena: ")
    print(longitud(inpot))
    
def longitud(inpot):
     contador = 0
     
     for _ in inpot:
         contador += 1
     return contador
        
       
    
    
main()