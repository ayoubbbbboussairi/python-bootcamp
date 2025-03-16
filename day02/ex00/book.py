import datetime
from datetime import datetime
from  recipe import Recipe

class book:
    def __init__(self,name,last_update = datetime.now(),creation_date =datetime.now()) :
        self.name = str(name)
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name() == name :
                    print(recipe)
                    return recipe
        return None 
    def get_recipes_by_types(self, recipe_type):
        """Obtient tous les noms de recettes pour un type de recette donné"""
        if recipe_type in self.recipes_list:
            recipes = self.recipes_list[recipe_type]
            if recipes:
                return [recipe.name for recipe in recipes]
            else:
                print(f"Aucune recette de type '{recipe_type}'.")
        else:
            print("Type de recette non valide.")
        return []
    def add_recipe(self, recipe):
        """Ajoute une recette au livre et met à jour last_update"""
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
            print(f"Recette '{recipe.name}' ajoutée avec succès.")
        else:
            print("Erreur : l'argument passé à add_recipe n'est pas une instance de Recipe.")