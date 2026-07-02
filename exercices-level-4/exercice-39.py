'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
 Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
 Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''


ingredientes_veg = ["pimiento", "tofu"]
ingredientes_noveg = ["peperoni", "jamon", "salmon"]
ingredientes_pizza = ["mozzarella", "tomate"]

def main():
    choice = input("Bienvenido a pizzeria  Bella Napoli, desea una pizza normal o vegetariana?\n")
    pizza_choice(choice)


def pizza_choice(choice):

    if choice == "vegetariana":
        print("menu:")
        for numero, ingredientes in enumerate(ingredientes_veg):
            print(numero, ingredientes)
        
        ingredientes_selec = input("seleccione un ingresiente del menu: ")

        if ingredientes_selec in ingredientes_veg:
            ingredientes_pizza.append(ingredientes_selec)

    elif choice == "normal":

        print("menu: ")
        for numero, ingredientes in enumerate(ingredientes_noveg):
            print(numero, ingredientes)
        
        ingredientes_selec = input("seleccione un ingresiente del menu: ")

        if ingredientes_selec in ingredientes_veg:
            ingredientes_pizza.append(ingredientes_selec)


    print(f"La pizza elegida es {choice}, y sus ingredientes son: {", ".join(ingredientes_pizza)}")


main()