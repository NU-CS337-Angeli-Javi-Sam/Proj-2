import copy
import random

from data_structures.ontologies.Ingredients import IngredientOntology
from data_structures.ontologies.Measurements import MeasurementsOntology

class SubstitutionOntologies:
    ingredients_ontology = IngredientOntology()
    measurements_ontology = MeasurementsOntology()

    def __init__(self):
        self.categories = {
            'vegetarian': {
                'Proteins': ['tofu', 'lentils', 'soybeans', 'chickpeas', 'tempeh']
            },
            'halal/kosher': {
            },
            'healthy': {
            },
            'mexican': {
            },
            'measurement': {
                ["\"\"", "in.", "inch", "in", "inches"] : "Centimeter", #Centimeters
                ["oz.", "ozs.", "ounce", 'ounces', 'oz'] : 'Gram', #Grams
                ["lb.", "lbs.", "pound"] : "Kilogram", #Kilograms
                ["F", "Fahrenheit", "fahrenheit", "f"] : "Celsius", #Celcius

                ["cm.", "centimeter", "cm", "centimeters"] : "Inch",  # Inches
                ['g.','g', 'gram', 'grams']: "Ounce",  # Ounces
                ['kg.','kg', 'kilogram', 'kilograms']: "Pound",  # Pounds
                ["C", "Celsius", "celsius", "c"]: "Fahrenheit"  # Fahrenheit
            }
        }

    """
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

    def substituteRecipe(self, variation, recipe):
        substituted = False

        if variation in self.categories.keys():
            # Get the correct variation dictionary, if it exists
            if variation == 'halal' or variation == 'kosher':
                variation_dict = self.categories['halal/kosher']
            elif variation == 'metric' or variation == 'imperial':
                variation_dict = self.categories['measurement']
                self.convertMeasurements(recipe, variation_dict)
                substituted = True
            else:
                variation_dict = self.categories[variation]

            if not substituted:
                self.convertDiet(recipe, variation_dict)
        else:
            return None

    def convertMeasurements(self, recipe, variation_dict):
        steps = recipe.get_instructions()

        for index in range(0, len(steps)):
            curr_step = steps.get_node_at(index)

            # Change ingredients
            step_ingredients = curr_step.get_

    def convertDiet(self, recipe, variation_dict):
        steps = recipe.get_instructions()
        ingredients = recipe.get_ingredients()

        #Change ingredients
        for name, ingredient in ingredients:
            #Get the category of the ingredient
            category = ingredients.get_category(ingredient.get_simplified_name())

            #If this category is relevant to our variation, change the name of ingredient
            #Add to new_ingredients list
            if category in variation_dict:

                #Grab random ingredient
                rand_int = random.randint(0, len(variation_dict[category])-1)

                #Key is new name of new ingredient
                new_name = variation_dict[category][rand_int]

                #Change original text to use the new name
                ingredient.get_original_text().replace(ingredient.get_full_name(), new_name)

                #Create copy of ingredient, change full name and simplified name
                ingredient.set_full_name(new_name)
                ingredient.set_simplified_name(new_name)

        for index in range(0, len(steps)):
            curr_step = steps.get_node_at(index)

            # Change ingredients
            step_ingredients = []

            #Change instructions
