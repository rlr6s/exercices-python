'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
 calcule el índice de masa corporal y lo almacene en una variable,
  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
   índice de masa corporal calculado
 redondeado con dos decimales. '''


def main():
    peso = float(input("cuanto pesas en kg:"))
    altura = float(input("cuanto mides en cm:"))
    
    altura2 = altura * altura
    imc = peso / altura2

    print(f"Tu índice de masa corporal es {imc:.2f} ")

main()
