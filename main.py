import requests

def dish_fetch(num):
    response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
    dishes = response.json()
    
    #Guardamos los platos en una lista
    dish = dishes[num]
    
    #Crea y devuelve un diccionario nuevo con solo esos datos del plato
    return {

    "id": num,
    "name": dish["name"],
    "description": dish["description"],
    "ingredients": dish["ingredients"]
}

    


def main():
    print("Comida tipica colombiana")
    
    eleccion = int(input("Dame un numero y te dije un plato tipico de mi pais "))
    
    seleccion = dish_fetch(eleccion)
    
    print("id:", seleccion["id"])
    print("Name:", seleccion["name"])
    print("Description:", seleccion["description"])
    print("Ingredients:", seleccion["ingredients"])


if __name__ == "__main__":
    main()