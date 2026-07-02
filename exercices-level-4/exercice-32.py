'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''
def main():
    edad = int(input("edad: "))
    
    if edad >= 18:
        print("mayor de edad")
    
    else:
        print("menor de edad")
    
    
main()
