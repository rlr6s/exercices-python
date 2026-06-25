'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience
 leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
 el precio habitual de una barra de pan,
 el descuento que se le hace por no ser fresca y el coste final total.'''
 
def main():
    precio_barra = 3.49
    descuento  = 0.60
    
    barras = (int(input("ingrese la cantidad de barras no frescas vendidas: ")))
    
    precio_descuento = precio_barra * descuento
    precio_final_barra = precio_barra - precio_descuento
    coste_total = barras * precio_final_barra
    
    print(f"el precio habitual de las barras son de {precio_barra}")
    print(f"descuento de la barra por no ser fresca: {descuento * 100}%")
    print(f"coste final: {coste_total:.2f}")
    
    
main()
    
    
    
     