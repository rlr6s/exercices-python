'''Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".'''



def main():
   caracter = (input("ingrese el caracter: "))
   n = int(input("ingrese el numero de veces que se repetira el caracter: "))
   print(generar_n_caracteres(n, caracter))

def generar_n_caracteres(n, caracter):
    return caracter * n

main()
