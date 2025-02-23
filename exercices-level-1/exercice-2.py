'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''


def main():
  mayor = max_de_tres()

  print(f"El numero mas grande es {mayor}")

def max_de_tres(mayor):
  a = int(input("ingrese el primer numero: "))
  b = int(input("ingrese el segundo numero: "))
  c = int(input("ingrese el tercer numero: "))

  if a > b and a > c:
        
        mayor = a
  elif b > c:
        mayor = b
        
  else: 
       mayor = c

  return mayor
    


main()

