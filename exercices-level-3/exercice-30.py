'''Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
 separados por comas, y muestre por pantalla
 cada uno de los productos en una línea distinta.'''

def main():
    
    cesta = input("ingrese los productos de su carrito: ").strip().lower().replace(" ","")
    
    carrito = cesta.split(",")
    
    
    for indice, valor in enumerate(carrito):
        print(indice, valor)
        
main()
        
        