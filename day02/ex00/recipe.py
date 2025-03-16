class Recipe:
    def __init__(self,name,cooking_lvl,cooking_time,ingredients,description,recipe_type) :
        self.name = str(name)
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = list(ingredients)
        self.description = str(description)
        self.recipe_type = str(recipe_type)
        self.validate_input()
    def validate_input(self):
        if not isinstance(self.name,str) or not self.name :
            raise ValueError ('la recette doit etre une strig non empty')
        if not isinstance(self.cooking_lvl,int) or not (1 < self.cooking_lvl < 5):
            raise ValueError ('lvl doit etre un entier et entre 1-5 ')
        if not isinstance(self.cooking_time,int) or not (self.cooking_time < 0):
            raise ValueError ('time doit etre un entier positif')
        if not isinstance(self.ingredients, list) or not all(isinstance(ingredient, str) for ingredient in self.ingredients):
            raise ValueError("Les ingrédients doivent être une liste de chaînes.")
        if not isinstance(self.description,str):
            raise ValueError('description doit etre string')
        if self.recipe_type not in ['starter','lunch','dessert']:
            raise ValueError('type doit soit starter lunch dessert')                                              
                                                         
        def __str__(self):
            txt = f"le nom de la recette {self.name}"
            txt += f"la dificule de la recete est {self.cooking_lvl}/5"
            txt += f"le time de la recette {self.cooking_time}"
            txt += f"la liste des ingredients{', '.join(self.ingredients)} "
            txt += f"la description est {self.description}"
            txt += f"le type de la recette est {self.recipe_type}"
            return txt