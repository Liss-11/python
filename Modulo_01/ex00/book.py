import datetime
from recipe import Recipe

class Book:

    def __init__(self, name, recipes_list):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        self.recipes_list = recipes_list if isinstance(recipes_list, dict(str, [Recipe])) else (print("Recipe list has an incorrect format"), exit(1))

    def get_recipe_by_name(self, name):
        """Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
        for recipe in self.recipes_list:
            if recipe.name == name:
                recipe.__str__()
                return recipe
        "This recipe is not available in this book"
        return (0)

    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        recipes = []
        for recipe in self.recipes_list:
            if recipe.recipe_type == recipe_type:
                recipes.append(recipe)
        return recipes

    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        self.recipes_list.append(recipe)
        self.last_update = datetime.datetime.now()

#me falta entender si lo que se anade son arrays de los diferentes tipos de postres, cuando creamos el diccionario es uno de cada, pero luego a;adimos alguno al tipo que queramos...?

#compromar si recibo correctamente un recipe!!!! ---------->isinstance(var, Recipe)<----------