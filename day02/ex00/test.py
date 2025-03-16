from recipe import Recipe
from book import book
from datetime import datetime
from time import sleep
book = book("fastFood", datetime.now(), datetime.now())
print(book)
tourte = Recipe("Cake", 1, 1, ["fole"], "best recipe", "lunch")
tourte1 = Recipe("Cake2", 1, 1, ["fole"], "best recipe", "lunch")
if tourte.recipeValed == True:
    book.add_recipe(tourte)
if tourte1.recipeValed == True:
    book.add_recipe(tourte1)
obj = book.get_recipe_by_name("Cake")
if obj == None:
    print("ERROR:")
all_recipe = book.get_recipes_by_types("lunch")
for recip in all_recipe:
    print("================================")
    print(recip)