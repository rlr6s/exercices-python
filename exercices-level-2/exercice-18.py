'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado.'''

def main():
    payasos =int(input("cuantos payasos desea comprar?: "))
    muñecas = int(input("cuantas muñecas desea comprar?: "))

    print("el peso total del pedido es de:", peso(payasos, muñecas), "gramos")
    
def peso(payasos, muñecas):
    
    peso_muñecas = 75
    peso_payasos = 112
    
    peso_total =  (peso_muñecas * muñecas) + (peso_payasos * payasos)
    
    return peso_total


main()  
    
    
    
    