'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

password = "password"

while True:

    user_pass = input("ingrese la contraseña: ")    

    if user_pass != password:
        print("intente de nuevo \n")
    else:
        print("excelente")
        break

