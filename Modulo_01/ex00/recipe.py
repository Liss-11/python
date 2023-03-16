class Recipe:
    
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name if isinstance(name, str) else (print("Name must be a String"), exit())
        self.cooking_lvl = cooking_lvl if (isinstance(cooking_lvl, int) and (int(cooking_lvl) >= 1 and int(cooking_lvl) <= 5)) else (print("Cooking_lvl must be a Number between 1 and 5"), exit(1))
        self.cooking_time = cooking_time if (isinstance(cooking_time, int) and int(cooking_time) >= 0) else (print("Cooking time must be a positive Number"), exit(1))
        for ingredient in ingredients:
            if not isinstance(ingredient, str):
                print("Ingredients must be only strings")
                exit (1)
        self.ingredients = ingredients
        self.description = description if (description == '' or isinstance(description, str)) else (print("Description must be a string"), exit(1))
        self.recipe_type = recipe_type if (isinstance(recipe_type, str) and (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert")) else (print("Recipy tipe must be: starter, lunch or dessert"), exit(1))
    
    def __str__(self):
        """Return the string to print with the recipe info""" 
        txt = "Recipe for " + self.name + ":\n\tCooking level: " + str(self.cooking_lvl)  + "\n\tIngredients list: " + str(self.ingredients) + "\n\tDescription: " + \
        self.description + "\n\tTo be eaten for: " + self.recipe_type + "\n\tCooking time: " + str(self.cooking_time) + " minuts"
        return txt