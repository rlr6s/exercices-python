'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience
 leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
 el precio habitual de una barra de pan,
 el descuento que se le hace por no ser fresca y el coste final total.'''


def main():
    print("bienvenido a mi panaderia")
    panaderia()
    print("gracias por su compra")



def panaderia():
    barra_ven = int(input("cuantas barras vendio: "))
    barra = 3.49
    descuento = 0.6

    precio_h = barra_ven * barra
    descuento_f = precio_h * descuento
    precio_final  = precio_h - descuento_f

    print(f"el precio habitual es: {precio_h:.2f}")
    print(f"se le hace un descuento de {descuento_f:.2f}")
    print(f"el precio final es de: {precio_final:.2f} ")


main()


