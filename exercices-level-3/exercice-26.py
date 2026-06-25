'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
 y después muestre por pantalla
 la misma frase pero con la vocal introducida en mayúscula'''
 
def main():
    frase = input("introduzca una frase: ")
    vocal = input("ahora introduzca una vocal: ").lower()
    
    
    nueva_frase = ""
    
    for letra in frase:
        if letra.lower() == vocal:
            nueva_frase += letra.upper()
        else:
            nueva_frase += letra
    
    print(nueva_frase)
            
main()