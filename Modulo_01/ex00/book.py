import datetime
from recipe import Recipe

class Book:

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}

    #Devuelve todas las recetas dado un recipe_type
    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipes_list:
            return self.recipes_list[recipe_type]
        print("Is not a valid recype type")
        return (1)

    def get_recipe_by_name(self, name):
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    return recipe
        print(f"Recipe '{name}' not found.")
        return (1)

    #Añade una receta al libro y actualiza last_update
    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("Is not a valid Recipe")
            return (1)
        if recipe.recipe_type in self.recipes_list:
                self.recipes_list[recipe.recipe_type].append(recipe)
                self.last_update = datetime.datetime.now()
        else:
            print("Not valid recipe type")