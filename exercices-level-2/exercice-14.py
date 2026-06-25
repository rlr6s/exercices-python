'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.'''

def main():
    horas = float(input("cuantas horas trabaja al dia: "))
    coste = float(input("cuanto le pagan por hora de trabajo: "))
    
    print("la paga total es: ",paga(horas, coste))
    
def paga(horas, coste):
    
    return horas * coste

main()