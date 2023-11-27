from repository.recipes import recipes
from uuid import UUID

def get_recipe_names(): 
    return [val.name for val in recipes.values()]

def get_recipe_ingredients(rid: UUID): 
    ingredients = recipes[rid].ingredients
    return ingredients