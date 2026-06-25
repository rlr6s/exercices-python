'''Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
******* '''

def main():
    
    entrada = input("ingrese 3 numeros: ")
    
    entrada = entrada.replace(" ", "")
    
    lista = list(map(int, entrada.split(",")))
    
    histograma(lista)
    
def histograma(lista):
    
    for numero in lista:
      print("*" * numero)
    
main()