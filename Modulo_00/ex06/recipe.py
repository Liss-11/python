import sys

cookbook =  {
    "bocadillo" : {
        "ingrediets" : ["jamón", "pan", "queso", "tomate"],
        "meal" : "almuerzo",
        "prep_time" : 15
    },
    "tarta" : {
        "ingrediets" : ["harina", "azúcar", "huevos"],
        "meal" : "postre",
        "prep_time" : 60
    },
    "ensalada" : {
        "ingrediets" : ["aguacate", "rúcula", "tomates", "espinacas"],
        "meal" : "almuerzo",
        "prep_time" : 15
    }
}

def print_book(book:dict):
    for x in book.keys():
        print(x)

def print_recipe(book:dict, name:str):
    my_recipe = dict(book.get(name))
    print("\nRecipe for " +  name + " :\n\t" + "Ingredients list: " + str(my_recipe.get("ingrediets")) + "\n\tTo be eaten for " + str(my_recipe.get("meal")) + ".\n\tTakes " + str(my_recipe.get("prep_time")) + " minutes of cooking.")


def del_item(book:dict, name:str):
    book.pop(name)

def new_recipe(book:dict) -> dict:
    name = input("Enter a name:")
    my_ingredients = input("Enter ingredients:").split()
    meal = input("Enter a meal type:")
    try:
        time = int(input("Enter a preparation time:"))
        if time < 0:
            print("Preparation time must be a POSITIVE number")
            exit(0)
    except:
        print("Preparation time must be a number")
        exit(0)
    book[name] = dict(ingredits = my_ingredients, meal = meal, prep_time = time)
    return book

def print_options():
    print("\nList of available option:\n\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit")


if __name__ == '__main__':
    print("\nWelcome to the Python Cookbook!")
    print_options()
    action = input("\nPlease select an option:\n")
    while action != "5":
        if action == "1":
            cookbook = new_recipe(cookbook)
        elif action == "2":
            item = input("\nPlease enter a recipe name to get its details:\n")
            del_item(cookbook, item)
        elif action == "3":
            name = input("\nPlease enter a recipe name to get its details:\n")
            print_recipe(cookbook, name)
        elif action == "4":
            print_book(cookbook)
        else:
            print("\nSorry, this option does not exist.")
            print_options()
        action = input("\nPlease select an option:\n")
    print("\nCookbook closed. Goodbye !")
    exit(0)



