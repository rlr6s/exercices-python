'''Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
 Adaptar el programa anterior para que también funcione cuando
 el día o el mes se introduzcan con un solo carácter.'''
 
def main():
    fecha = input("ingrese una fecha dd/mm/aaaa: " )
    
    partes = fecha.split("/")
    
    Dia = partes[0]
    Mes = partes[1]
    Año = partes[2]
    
    print(f"Dia: {Dia}")
    print(f"Mes: {Mes}")
    print(f"Año: {Año}")
    
    
main()
    
     