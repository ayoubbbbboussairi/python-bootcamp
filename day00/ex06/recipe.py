cookbook = {
    'sandwich' : {
        'ingredients' : ['ham','bread','cheese','tomatoes'],
        'meal' : 'lunch',
        'prep_time' : 10
    },
    'cake' : {
        'ingredients' : ['flour','sugar','eggs'],
        'meal' : 'dessert',
        'prep_time' : 60
    },
    'salad' : {
        'ingredients' : ['avocado','arugula','tomatoes','spinach'],
        'meal' : 'lunch',
        'prep_time' : 15
    }
}
def name_recipe(cookbook):
    for name in cookbook :
        print(name)
def details_recipe (cookbook,name):
    if name in cookbook:
        recipe_details = cookbook[name]
        print(f"Details de la recette '{name}':")
        print(f"Ingredients: {recipe_details['ingredients']}")
        print(f"Type de repas: {recipe_details['meal']}")
        print(f"Temps de préparation: {recipe_details['prep_time']} minutes")
    else:
        print(f"La recette '{name}' n'est pas dans le cookbook.")

def del_recipe(cookbook,name):
    if name in cookbook:
        del cookbook[name]
        print('la reccete est supp')
    else :
        print('la reccete n est pas supp elle n a pas existe')

def add_recipe(cookbook):
    name = input("Entrez le nom de la recette : ")
    ingredients = input("Entrez la liste d'ingrédients  : ")
    meal_type = input("Entrez le type de repas : ")
    prep_time = int(input("Entrez le temps de préparation (en minutes) : "))
    
    new_recipe = {
        "ingredients": [ingredients.strip()],
        "meal": meal_type,
        "prep_time": prep_time
    }
    cookbook[name] = new_recipe

def main():
    while True:

        n = int(input("Welcome to the Python Cookbook !\nList of available option:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n\n\nPlease select an option:"))
        if n == 1:
            add_recipe(cookbook)
        elif n == 2: 
            name = input("name of recipe to delete: ")
            del_recipe(cookbook,name)
        elif n == 3 :
            name = input("name of recipe to show details: ")
            details_recipe (cookbook,name)
        elif n == 4:
            print(cookbook)
        elif n == 5:
            break
        else :
            print("invalid option please chose (1 to 5)")

if __name__ == "__main__":
    main()




#del_recipe(cookbook,'salad')
#name_recipe(cookbook)
#details_recipe(cookbook,'salad')
#add_recipe(cookbook)
#print(cookbook)