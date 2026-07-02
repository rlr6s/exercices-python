'''Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus 
ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. '''

def main():
    edad = int(input("ingrese su edad: "))
    ingreso = int(input("ingrese su ingreso mensual: "))

    tributo(edad, ingreso)


def tributo(edad, ingreso):
    if edad <= 16 or ingreso < 1000:
        print("no tributa")

    else:
        print("debe tributar")

main()