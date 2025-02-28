'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''
def sum ():
  
  num = [1,2,3,4]
  total = 0
  for i in num:
    total += i
    
  return total 
  
def multip():
  num = [1,2,3,4]
  total  = 1
  for i in num:
    total *= i
  return total
  
