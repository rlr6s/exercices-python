'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.'''


def main():
    cp = int(input("ingrese una cantidad a invertir: "))
    tasa = int(input("ingrese el interes anual: "))
    tiempo = int(input("ingrese cuantos años durara al inversion: "))

    total = cp
    for año in range(1, tiempo + 1):
        ganancia = cp * tiempo * (tasa / 100)
        total += ganancia
        print(f"año {año}: {total}")
    

main()
    




