'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.'''


def main():
    correo = input("ingrese su correo electronico: ").strip().replace(" ","")
    
    partes = correo.split("@")
    nombre = partes[0]
    
    nuevo_correo = nombre + "@ceu.es"
    
    print(nuevo_correo)
    
    
main()