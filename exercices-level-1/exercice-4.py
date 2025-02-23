'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''

def main():
  si_o_no = vocal()
  print(si_o_no)
  
def vocal():
  while True:
    try:
        caracter = input("introduce un caracter: ")
        if caracter.lower() in "aeiou":
            return True
        else:
            print("no es una vocal")
    except EOFError:
        pass       
        break
    
main()

