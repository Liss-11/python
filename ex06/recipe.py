import sys
import numpi
import numpy as np

#recipe = dict(ingredits = ["jamón", "pan", "queso", "tomate"], meal = "almuerzo", prep_time = 15)

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

def print_keys(book:dict):
    for x in book.keys():
        print(x)

def get_recipy(book:dict, name:str):
    my_recipe = dict(book.get(name))
    print("Recipe for " +  name + " :\n\t" + "Ingredients list: " + str(my_recipe.get("ingrediets")) + "\n\tTo be eaten for " + str(my_recipe.get("meal")) + ".\n\tTakes " + str(my_recipe.get("prep_time")) + " minutes of cooking.")


def del_item(book:dict, name:str):
    book.pop(name)

def new_recipe(book:dict) -> dict:
    name = input("Enter a name:")
    my_ingredients = input("Enter ingredients:").split
    meal = input("Enter a meal type:")
    try:
        time = int(input("Enter a preparation time:"))
        if time < 0:
            print("Preparation time must be a POSITIVE number")
            exit(0)
    except:
        print("Preparation time must be a number")
        exit(0)
    book[name] = dict(ingredits = [], meal = meal, prep_time = time)
    #book[name]["ingredits"].append("patatas")
    #for i in ingredients:
    #    print(i)
    #i = 0    
    #while i < len(my_ingredients):
    #    print(my_ingredients[i])
    #for i in ingredients:
        #book[name]["ingredits"].append(i)
    print(my_ingredients)
    print(book[name])
    return book



print_keys(cookbook)
get_recipy(cookbook, "tarta")
del_item(cookbook, "bocadillo")
new_recipe(cookbook)

#for recipe in cookbook:
#    print(str(recipe))



