'''Escribir un programa que pregunte por consola el precio de un
 producto en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.'''


def main():
    precio = (input(f"ingrese el precio del producto: ")).strip().replace(" ","")
    
    partes = precio.split(".")

    if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit() and len(partes[1]) == 2:
        euros = partes[0]
        centavos = partes[1]
        
        print(f"euros: {euros}, centavos: {centavos}")
        
    else:
        print("formato incorrecto")
        
        
main()