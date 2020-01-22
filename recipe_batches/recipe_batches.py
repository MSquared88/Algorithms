#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    #take each recipe item and devide it by the igredients available
    #whatever the lowest num is that is how many batches we can make
    recipe_keys = recipe.keys()

    batches = float("inf")
    for i in recipe_keys:
        
        if ingredients.get(i) == None:
            return 0 

        recipe_value = recipe.get(i)
        ingredient_value = ingredients.get(i)
        ingredient_batch = ingredient_value // recipe_value

        if ingredient_batch < batches:
            batches = ingredient_batch
        
    return batches
    



# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test 
#     # your implementation with different inputs
#     recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#     ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))