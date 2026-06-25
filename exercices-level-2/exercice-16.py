'''Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
 entera respectivamente. '''
 
def main():
    n = int(input("ingrese un numero entero: "))
    m = int(input("ingrese otro numero entero: "))
    
    cociente = n // m
    resto = n % m 
    
    print("el cociente es:", cociente ,", y el resto es:", resto)
    
main()
     