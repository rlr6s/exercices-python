'''Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
 de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al
  usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede 
  entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€. '''


def main():
    edad = int(input("ingrese su edad: "))
    print(costo_entrada(edad))

def costo_entrada(edad):

    if edad <  4:
        return "entrada gratis"
    elif edad <= 18:
        return "entrada: 5 euros"
    
    else:
        return "entrada: 10 euros"


main()