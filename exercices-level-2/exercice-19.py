'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad
 de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y
  mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
 Redondear cada cantidad a dos decimales.'''


def main():
    print("Bienvenido al programa de cálculo de cuenta de ahorros")
    banco()

def banco():
    cuenta_ahorros = int(input("Ingrese el monto de su cuenta de ahorros: "))

    primer_ano = cuenta_ahorros + (cuenta_ahorros * 0.04)
    segundo_ano = primer_ano + (primer_ano * 0.04)
    tercer_ano = segundo_ano + (segundo_ano * 0.04)

    print(f"""El monto de su cuenta de ahorros después de 1 año es: {primer_ano},
     después de 2 años es: {segundo_ano} 
     y después de 3 años es: {tercer_ano}""")


main()



