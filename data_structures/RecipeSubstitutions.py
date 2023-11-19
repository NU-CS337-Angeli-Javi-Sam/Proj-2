import copy
from data_structures.ontologies.Ingredients import IngredientOntology
from utils.create_recipe import create_recipe
import random

"""
    Food Categories:
            "Fruits"
            "Vegetables"
            "Proteins"
            "Grains"
            "Dairy"
            "Herbs and Spices"
            "Oils and Condiments"
            "Canned and Packaged"
            "Nuts and Seeds"
            "Sweets and Desserts"
"""

ingredientOnt = IngredientOntology()

categories = {
    'vegetarian': {
        #Change back to Proteins
        'Vegetables': ['tofu', 'lentils', 'soybeans', 'chickpeas', 'tempeh']
    },
    'halal/kosher': {
    },
    'healthy': {
    },
    'mexican': {
    },
    'measurement': {
        ("\"\"", "in.", "inch", "in", "inches"): "centimeter",  # Centimeters
        ("oz.", "ozs.", "ounce", 'ounces', 'oz'): 'gram',  # Grams
        ("lb.", "lbs.", "pound"): "Kilogram",  # Kilograms
        ("F", "Fahrenheit", "fahrenheit", "f"): "celsius",  # Celcius

        ("cm.", "centimeter", "cm", "centimeters"): "inch",  # Inches
        ('g.', 'g', 'gram', 'grams'): "Ounce",  # Ounces
        ('kg.', 'kg', 'kilogram', 'kilograms'): "pound",  # Pounds
        ("C", "Celsius", "celsius", "c"): "fahrenheit"  # Fahrenheit
    }
}


def substitute_recipe(variation, recipe_data, recipe):
    # Get the variation requested by the user and format it for our categories dictionary
    # Determine whether to replace ingredients or measurements
    replacingIngredients = True

    variation = variation.lower()
    if variation == 'halal' or variation == 'kosher':
        variation = 'halal/kosher'
    elif variation == 'imperial' or variation == 'metric':
        variation = 'measurement'
        replacingIngredients = False

    #Get the variation the user is looking for
    variation_dict = categories[variation]

    # Replace all the ingredients or measurements for our recipe
    if replacingIngredients:
        old_ingredients_dict = recipe.get_ingredients()

        new_recipe_data = __substitute_ingredients(variation_dict, old_ingredients_dict, recipe_data)
    else:
        new_recipe_data = __substitute_measurments()

    # Create new recipe from new_recipe_data
    # recipe = None
    # if new_recipe_data:
    #     recipe = create_recipe(new_recipe_data)
    # return recipe

def __substitute_ingredients(variation_dict, old_ingredients_dict, recipe_data):
    #https://www.epicurious.com/recipes/food/views/mashed-potatoes-recipe

    new_recipe_data = copy.deepcopy(recipe_data)

    #New dictionary mapping old ingredients to their replacement
    new_ingredients_dict = {}

    for k, v in old_ingredients_dict.items():
        # Map old ingredients (simple name and full name) to new replacements, if applicable

        # Get an ingredient of the same category as the old ingredient
        category = ingredientOnt.get_category(k)
        if category in variation_dict:
            #Map all ingredients to their replacement, randomly choose an integer
            max_int = len(variation_dict[category])
            replacement = variation_dict[category][random.randint(0, max_int)-1]

            new_ingredients_dict[(v.get_full_name(), k)] = replacement

    #Replace all instances of ingredient in recipeIngredients
    for index, instance in enumerate(new_recipe_data['recipeIngredient']):

        for ingredient_name, replacement in new_ingredients_dict.items():
            if ingredient_name[0] in instance:
                instance = instance.replace(ingredient_name[0], replacement)
            elif ingredient_name[1] in instance:
                instance = instance.replace(ingredient_name[1], replacement)
        new_recipe_data['recipeIngredient'][index] = instance

    for index, instance in enumerate(new_recipe_data['recipeInstructions']):
        for ingredient_name, replacement in new_ingredients_dict.items():
            if ingredient_name[0] in instance['text']:
                instance['text'] = instance['text'].replace(ingredient_name[0], replacement)
            elif ingredient_name[1] in instance['text']:
                instance['text'] = instance['text'].replace(ingredient_name[1], replacement)
        new_recipe_data['recipeInstructions'][index] = instance

    return new_recipe_data

def __substitute_measurments():
    return None
