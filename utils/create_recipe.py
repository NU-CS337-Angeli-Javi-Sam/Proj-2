from typing import Any, List
# import nltk
from nltk.tokenize import sent_tokenize

from data_structures.Recipe import Recipe
from parsers.parse_ingredient import parse_ingredient
from parsers.parse_instruction import parse_instruction
from parsers.parse_time import parse_time
from data_structures.Instruction import Instruction
from data_structures.Ingredient import Ingredient
from data_structures.ontologies.Measurements import MeasurementsOntology

# nltk.download('punkt')
measurements = MeasurementsOntology()

def get_and_set_recipe_name(recipe: Recipe, recipe_data: Any) -> None:
    recipe_name: str = recipe_data["name"]


    recipe.set_name(recipe_name)

def get_and_set_recipe_ingredients(recipe: Recipe, recipe_data: Any) -> None:
    recipe_ingredients: List["str"] = []

    #Temp structure, wasn't sure where to add the ingredient dictionary obj so I put it here - Sam
    #String(Ingredient original name) to Ingredient obj (parsed ingredient)
    recipe_ingredients_dict = {}

    for ingredient in recipe_data["recipeIngredient"]:
        recipe_ingredients.append(ingredient)

    for ingredient in recipe_ingredients:
        if "Special Equipment" in ingredient:
            continue

        # Remove measurement abbreviations
        ingredient_sent_lst = ingredient.split(" ")
        for i in range(len(ingredient_sent_lst)):
            measurement_category = measurements.get_category(ingredient_sent_lst[i])
            if measurement_category != "Unknown":
                ingredient_sent_lst[i] = measurement_category

        ingredient_sent = sent_tokenize(" ".join(ingredient_sent_lst))[0]
        # print(ingredient_sent)

        #Construct ingredient object and place into ingredient dictionary
        parsed_ingredient = Ingredient(ingredient_sent)

        recipe_ingredients_dict[ingredient_sent] = parsed_ingredient

    recipe.add_ingredients(recipe_ingredients_dict)


def get_and_set_recipe_instructions(recipe: Recipe, recipe_data: Any) -> None:
    recipe_instructions: List["str"] = []
    recipe_prep_notes: List["str"] = []

    # print("Recipe Instructions: \n")
    count = 1
    for instruction in recipe_data["recipeInstructions"]:
        # Grab text for each individual instruction
        instruction_text: str = instruction["text"]
        if instruction_text == None:
            continue

        instr = instruction_text
        # Handle "Do Ahead:" in instructions
        if len(instruction_text.split("\nDo Ahead: ")) == 2:
            instr, extra_note = instruction_text.split("\nDo Ahead: ")

            # Remove Editor's note
            if len(extra_note.split("\n\nEditor's note: ")) == 2:
                extra_note, _ = extra_note.split("\n\n")
                recipe_prep_notes.append(extra_note)
            else:
                recipe_prep_notes.append(extra_note)

        # Replace measurement abbreviations to facilitate sentence splitting
        instruction_text_lst = instr.split(" ")
        for i in range(len(instruction_text_lst)):
            measurement_category = measurements.get_category(instruction_text_lst[i])
            if measurement_category != "Unknown":
                instruction_text_lst[i] = measurement_category

        sentences = sent_tokenize(" ".join(instruction_text_lst))
        recipe_instructions.extend(sentences)

    recipe.add_instructions(recipe_instructions)

    # Go through each of the instructions and make Instruction objects that we add to our doubly-linked list in Recipe


    # Get recipe prep notes

def get_and_set_recipe_cook_time(recipe: Recipe, recipe_data: Any) -> None:
    recipe_cook_time: str = recipe_data["cookTime"]


def get_and_set_recipe_total_time(recipe: Recipe, recipe_data: Any) -> None:
    recipe_total_time: str = recipe_data["totalTime"]


def get_and_set_recipe_yield(recipe: Recipe, recipe_data: Any) -> None:
    # Not sure at the moment what to do with this/what exact data we wanna extract from this
    recipe_yield: str = recipe_data["recipeYield"]


def create_recipe(recipe_data):
    recipe: Recipe = Recipe()

    get_and_set_recipe_name(recipe, recipe_data)
    get_and_set_recipe_ingredients(recipe, recipe_data)
    get_and_set_recipe_instructions(recipe, recipe_data)
    get_and_set_recipe_cook_time(recipe, recipe_data)
    get_and_set_recipe_total_time(recipe, recipe_data)
    get_and_set_recipe_yield(recipe, recipe_data)

    return recipe
