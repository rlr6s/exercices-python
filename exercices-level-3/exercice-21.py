'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como 
el número introducido.'''

def main():
    
    nombre = input("ingrese su nombre: ")
    numero = int(input("ingrese un numero entero: "))
    
    contador = 0
    
    while contador < numero:
        print(nombre)
        contador += 1
        
        
main()
        
    
    