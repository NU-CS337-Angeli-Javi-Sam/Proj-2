import copy

import unicodedata

from data_structures.ontologies.Ingredients import IngredientOntology
from utils.create_recipe import create_recipe
import random
import re

ingredientOnt = IngredientOntology()

categories = {
    #For testing
    'test': {
            "Fruits" : ['apple', 'orange'],
            "Vegetables" : ['broccoli', 'onions'],
            "Proteins" : ['chicken', 'beef'],
            "Grains" : ['bread', 'oats'],
            "Dairy" : ['cheese', 'milk'],
            "Herbs and Spices" : ['black pepper', 'oregano'],
            "Oils and Condiments" : ['olive oil', 'ketchup'],
            "Canned and Packaged" : ['canned tomatoes', 'canned corn'],
            "Nuts and Seeds" : ['peanut', 'walnut'],
            "Sweets and Desserts" : ['chocolate', 'cookie']
    },
    'vegetarian': {
        #Change back to Proteins
        "Proteins": ['tofu', 'lentils', 'soybeans', 'chickpeas', 'tempeh']
    },
    'halal/kosher': {
        "Proteins": ['chicken', 'beef', 'lamb', 'mackerel', 'salmon', 'tilapia', 'tuna'],
        'Liquor': ['broth']
    },
    'healthy': {
            "Proteins" : ' low-fat ',
            "Grains" : ' gluten-free ',
            "Dairy" : ' low-fat ',
            "Oils and Condiments" : ' low-fat ',
            "Sweets and Desserts" : ' low-sugar '
    },
    'mexican': {
        "Vegetables": ['tomato', 'bell pepper', 'jalapeno', 'poblano', 'habanero'],
        "Proteins": ['chorizo', 'al pastor', 'carne asada'],
        "Herbs and Spices" : ['cumin', 'cilantro', 'chili powder', 'oregano', 'paprika', 'garlic', 'cinnamon']
    },
    #Official unit name placed at beginning of the list
    'metric': {
        (" inch ", "\" ", " in. ", " inches ", "-inch ", "-in. "): " centimeter ",  # Centimeters
        (" ounce ", " oz. ", " ozs. ", ' ounces ', ' oz ', "-ounce ", "-oz. "): ' gram ',  # Grams
        (" pound ", " lb. ", " lbs. ", " pounds ", "-pound ", "-lb. "): " kilogram ",  # Kilograms
        (" fahrenheit ", " fahrenheit ", " F ", " f "): " celsius ",  # Celcius
    },
    'imperial': {
        (" centimeter ", " cm. ", " cm ", " centimeters "): " inch ",  # Inches
        (' gram ', ' g. ', ' g ', ' grams '): " Ounce ",  # Ounces
        (' kilogram ', ' kg. ', ' kg ', ' kilograms '): " pound ",  # Pounds
        (" celsius ", " C ", " Celsius ", " c "): " fahrenheit "  # Fahrenheit
    }
}

def __convertNumber(goal_measurement, old_number):
    #The measurement_type received is the measurement we are changing to,
    #assume that the number we get needs to be changed to it the measurement type we have
    new_number = 0

    #Temperature:
    # C -> F: (C × 9/5) + 32 = F
    if goal_measurement == 'fahrenheit':
        new_number = (old_number * 9 / 5) + 32
    # F -> C: (F − 32) × 5 / 9 = C
    elif goal_measurement == 'celsius':
        new_number = (old_number - 32) * 5 / 9

    #Inches/Centimeters
    # Cm -> In : cm / 2.54
    elif goal_measurement == 'inch':
        new_number = old_number / 2.54
    # In -> Cm : in * 2.54
    elif goal_measurement == 'centimeter':
        new_number = old_number * 2.54

    #Ounces/Grams
    # G -> Oz : g / 28.35
    elif goal_measurement == 'ounce':
        new_number = old_number / 28.35
    # Oz -> G : oz * 28.35
    elif goal_measurement == 'gram':
        new_number = old_number * 28.35

    #Pounds/Kilograms
    # kg -> lb : kg * 2.205
    elif goal_measurement == 'pound':
        new_number = old_number * 2.205
    # lb -> kg : lb / 2.205
    elif goal_measurement == 'kilogram':
        new_number = old_number / 2.205

    return round(new_number, 2)

def substitute_recipe(variation, recipe_data, recipe):
    # Get the variation requested by the user and format it for our categories dictionary
    # Determine whether to replace ingredients or measurements
    replacingIngredients = True

    variation = variation.lower()
    if variation == 'halal' or variation == 'kosher':
        variation = 'halal/kosher'
    elif variation == 'imperial' or variation == 'metric':
        replacingIngredients = False

    #Get the variation the user is looking for
    variation_dict = categories[variation]

    # Replace all the ingredients or measurements for our recipe
    if replacingIngredients:
        old_ingredients_dict = recipe.get_ingredients()

        new_recipe_data = __substitute_ingredients(variation_dict, old_ingredients_dict, recipe_data)
    else:
        new_recipe_data = __substitute_measurements(variation_dict, recipe_data)

    # Create new recipe from new_recipe_data
    recipe = None
    if new_recipe_data:
        recipe = create_recipe(new_recipe_data)
    return recipe


# Fix the 's' and 'es' stuff
# Fix the chicken broth problem
def __substitute_ingredients(variation_dict, old_ingredients_dict, recipe_data):
    #https://www.epicurious.com/recipes/food/views/mashed-potatoes-recipe

    new_recipe_data = copy.deepcopy(recipe_data)

    #list(dict_test.keys())[list(dict_test.values()).index('bear')]

    #New dictionary mapping old ingredients to their replacement
    new_ingredients_dict = {}

    for k, v in old_ingredients_dict.items():
        # Map old ingredients (simple name and full name) to new replacements, if applicable

        # Get an ingredient of the same category as the old ingredient
        category = ingredientOnt.get_category(k)

        if list(categories.keys())[list(categories.values()).index(variation_dict)] == 'healthy':
            if category in variation_dict:
                replacement = variation_dict[category] + k

            new_ingredients_dict[(v.get_full_name(), k)] = replacement
        else:
            # print(k)
            if category in variation_dict:
                #If the ingredient isn't accepted by our variation, i.e it doesn't appear under a variation_dict category
                #Map all ingredients to their replacement, randomly choose an integer
                if k in variation_dict[category]:
                    replacement = k
                else:
                    max_int = len(variation_dict[category])
                    replacement = variation_dict[category][random.randint(0, max_int)-1]

                new_ingredients_dict[(v.get_full_name(), k)] = replacement

    #Replace all instances of ingredient in recipeIngredient
    for index, instance in enumerate(new_recipe_data['recipeIngredient']):

        for ingredient_name, replacement in new_ingredients_dict.items():
            if ingredient_name[0] in instance:
                instance = instance.replace(ingredient_name[0], replacement)
            elif ingredient_name[1] in instance:
                instance = instance.replace(ingredient_name[1], replacement)
        new_recipe_data['recipeIngredient'][index] = instance

    #Replace all instances of ingredient in recipeInstructions
    for index, instance in enumerate(new_recipe_data['recipeInstructions']):
        for ingredient_name, replacement in new_ingredients_dict.items():
            if ingredient_name[0] in instance['text']:
                instance['text'] = instance['text'].replace(ingredient_name[0], replacement)
            elif ingredient_name[1] in instance['text']:
                instance['text'] = instance['text'].replace(ingredient_name[1], replacement)
        new_recipe_data['recipeInstructions'][index] = instance

    return new_recipe_data

def __substitute_measurements(variation_dict, recipe_data):
    new_recipe_data = copy.deepcopy(recipe_data)

    # Replace all instances of old measurement in recipeIngredients
    for index, instance in enumerate(new_recipe_data['recipeIngredient']):
        changed_measurements = []

        for measurements, replacement in variation_dict.items():
            for measure in measurements:
                if measure in instance:
                    instance = instance.replace(measure, replacement)

                    #Add the name of the measurement we changed to, i.e. if we are going from pound to kilo,
                    #kilo is saved here
                    changed_measurements.append(replacement.replace(' ', ''))

        #Check if any measurements changed
        if changed_measurements:
            instance_words = instance.split()

            #For every measurement changed, look for its place in the instance sentence
            for goal_measurement in changed_measurements:
                i = instance_words.index(goal_measurement)

                #Check if there's a number before our measurement unit
                old_number = unicodedata.normalize('NFKC', instance_words[i - 1])
                if i - 1 >= 0 and old_number[0].isdigit():
                    #If its all numbers convert it
                    if old_number.isdigit():
                        instance_words[i - 1] = str(__convertNumber(goal_measurement, int(old_number)))
                    else:
                        # If its not all numbers but has a '/' in it, it might be a fraction
                        old_number = old_number.replace('⁄', '/')

                        if '/' in old_number:
                            instance_words[i - 1] = str(__convertNumber(goal_measurement, eval(old_number)))
                        elif 'x' in old_number:
                            # If its not a all numbers, but has an 'x' in it, convert the number separate as it might be a 'by' measurement
                            old_number = old_number.split('x')
                            old_number[0] = str(__convertNumber(goal_measurement, int(old_number[0])))
                            old_number[2] = str(__convertNumber(goal_measurement, int(old_number[2])))

                            old_number = "".join(old_number)

            instance = " ".join(instance_words)

        new_recipe_data['recipeIngredient'][index] = instance

    # Replace all instances of old measurement in recipeIngredients
    for index, instance in enumerate(new_recipe_data['recipeInstructions']):
        changed_measurements = []
        for measurements, replacement in variation_dict.items():
            for measure in measurements:
                if measure in instance['text']:
                    instance['text'] = instance['text'].replace(measure, replacement)

                    # Add the name of the measurement we changed to, i.e. if we are going from pound to kilo,
                    # kilo is saved here
                    changed_measurements.append(replacement.replace(' ', ''))

        # Check if any measurements changed
        if changed_measurements:
            instance_words = instance['text'].split()

            # For every measurement changed, look for its place in the instance sentence
            for goal_measurement in changed_measurements:
                indices = [i for i, v in enumerate(instance_words) if v == goal_measurement]

                for i in indices:
                    # Check if there's a number before our measurement unit
                    old_number = unicodedata.normalize('NFKC', instance_words[i - 1])
                    if i - 1 >= 0 and old_number[0].isdigit():
                        # If its all numbers convert it
                        if old_number.isdigit():
                            instance_words[i - 1] = str(__convertNumber(goal_measurement, int(old_number)))
                        else:
                            # If its not all numbers but has a '/' in it, it might be a fraction
                            old_number = old_number.replace('⁄', '/')

                            if '/' in old_number:
                                instance_words[i - 1] = str(__convertNumber(goal_measurement, eval(old_number)))
                            elif 'x' in old_number:
                                # If its not a all numbers, but has an 'x' in it, convert the number separate as it might be a 'by' measurement
                                old_number = old_number.split('x')

                                old_number[0] = str(__convertNumber(goal_measurement, int(old_number[0])))
                                old_number[1] = str(__convertNumber(goal_measurement, int(old_number[1])))

                                old_number = "x".join(old_number)
                                instance_words[i - 1] = old_number

            instance['text'] = " ".join(instance_words)

        new_recipe_data['recipeInstructions'][index] = instance

    # print(new_recipe_data['recipeIngredient'])
    # print(new_recipe_data['recipeInstructions'])
    return new_recipe_data
