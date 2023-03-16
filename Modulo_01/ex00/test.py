from book import Book
from recipe import Recipe

if __name__=='__main__':
   
    poma = Recipe( 'poma', 3, 6, ["patata", "pome"], '', "dessert")
    #print(poma.__str__())

    book1 = Book("alissia")
    #print(book1.name)

    # name, cooking_lvl, cooking_time, ingredients, description, recipe_type
    recipe1 = Recipe("manzana", 3, 59, ["apple", "juce"], "very good", "dessert")
    recipe2 = "hola"
    print(recipe1.__str__())
    print(book1.recipes_list.keys())
    #book1.get_recipe_by_name("manzana")
    book1.add_recipe(recipe1)
    print(book1.get_recipe_by_name("manzana").__str__())
    #book1.get_recipe_by_name("manzana")