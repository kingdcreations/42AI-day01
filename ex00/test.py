from book import Book
from recipe import Recipe
from datetime import datetime


dict = {}
dict.update({'starter': []})
dict.update({'lunch': []})
dict.update({'dessert': []})

tourte = Recipe("Tourte", 1, 5, ["viande", "pate"], "C'est tres bon", "lunch")
salade = Recipe("Salade", 1, 5, ["tomate", "oignons"], "HMM", "lunch")
tarte = Recipe("Tarte a la framboise", 1, 5, [
               "framboises", "pate"], "", "dessert")
# to_print = str(tourte)
# print(to_print)

print()
bk = Book("name", datetime.now(), datetime.now(), dict)
Book.add_recipe(bk, tourte)
Book.add_recipe(bk, tarte)
Book.add_recipe(bk, salade)
Book.get_recipes_by_types(bk, 'lunch')
Book.get_recipes_by_types(bk, 'dessert')
Book.get_recipe_by_name(bk, 'Salade')
