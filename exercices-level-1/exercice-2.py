'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''

def main():
    a  = float(input("ingrese un numero: "))
    b = float(input("ingrese otro numero: "))
    c= float(input("ingrese otro numero mas: "))
    print("el numero mayor es:", max(a,b,c))

def max(a,b,c):
    
    if a >=b and a >=c:
        return a
    elif b >=a and b >=c:
        return b 
    else:
        return c
    
    
    
main()    
