'''Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla 
el capital obtenido en la inversión.'''

def main():
    
    capital = float(input("ingrese el capital inical: "))
    interes = float(input("ingrese el interes anual: "))
    tiempo = float(input("ingrese el numero de años: "))
    
    interes = interes / 100
    
    Cf = capital * (1 + interes * tiempo)
    
    print("el capital obtenido fue de:", Cf)
    
main()