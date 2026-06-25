'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''

def main(): 
    num = [1,2,3,4]
    print(sum(num))
    print(mult(num))
def sum (num):
    total = 0
    for i in num:
        total += i 
    return total 

def mult(num):
    total = 1
    for i in num:
        total *=i
    return total 
        
    
    
main()
    