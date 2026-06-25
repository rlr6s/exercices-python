'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
 calcule el índice de masa corporal y lo almacene en una variable,
  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
   índice de masa corporal calculado
 redondeado con dos decimales. '''
 
def main():
   
  peso = float(input("ingrese se peso en kg: "))
  estatura = float(input("ingrese su estatura en m: "))
  
  imc = peso / (estatura ** 2)
  
  print(f" su indice de grasa corparal es de: {imc:.2f}")
  
main()
  
