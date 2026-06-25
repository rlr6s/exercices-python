'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''
def main():
    edad = int(input("edad: "))
    
    if not edad >= 18:
        print("menor de edad")
    
    print("mayor de edad")
    
    
main()
    