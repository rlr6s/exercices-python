'''Escribir un programa que almacene la cadena de caracteres contraseña 
en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''


def main():
    contraseña = "password"
    contra_true = input("ingrese la contraseña: ").strip().lower()
    
    if contra_true != contraseña:
        print("intente de nuevo")

    else:
        print("contraseña correcta")

    

main()