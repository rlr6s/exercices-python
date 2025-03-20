'''Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
 entera respectivamente. '''

m = float(input("ingrese un numero: "))
n = float(input("ingrese un numero: "))

c = n // m
r = n % m

print(f"cociente es {c}")
print(f'el resto es {r}')
          
