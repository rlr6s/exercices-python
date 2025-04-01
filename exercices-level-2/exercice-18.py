'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado.'''

def main():


    print("Bienvenido al programa de cálculo de peso de paquetes")
    print("-----------------------------------------------------")

    pedido()

    print("-----------------------------------------------------")
    print("Gracias por usar nuestro programa")

def pedido():
    peso_muñeca = 75
    peso_payaso= 112

    num_muñecas = int(input("Introduce el número de muñecas: "))
    num_payasos = int(input("Introduce el número de payasos: "))

    peso_total = (num_muñecas * peso_muñeca) + (num_payasos * peso_payaso)

    print(f"el peso total del paquete es:{peso_total}")


main()
