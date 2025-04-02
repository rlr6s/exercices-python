'''Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
 El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. '''

def main():
    nombre_completo = input("Ingrese su nombre completo: ")

    nombre_mayusculas = nombre_completo.upper()
    nombre_minusculas = nombre_completo.lower()
    palabras = nombre_completo.split()
    nombre_formateado = " ".join(palabra.capitalize() for palabra in palabras)

    print(f"Nombre en mayúsculas: {nombre_mayusculas}")
    print(f"Nombre en minúsculas: {nombre_minusculas}")
    print(f"Nombre formateado: {nombre_formateado}")

main()
