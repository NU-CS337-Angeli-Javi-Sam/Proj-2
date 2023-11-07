from typing import List
import nltk
from nltk.tokenize import sent_tokenize

from data_structures.Recipe import Recipe
from parsers.parse_ingredient import parse_ingredient
from parsers.parse_instruction import parse_instruction
from parsers.parse_time import parse_time
from data_structures.ontologies.Measurements import MeasurementsOntology

nltk.download('punkt')
measurements = MeasurementsOntology()

def create_recipe(recipe_data):
    recipe: Recipe = Recipe()

    recipe_name: str = recipe_data["name"]
    recipe_ingredients: List["str"] = []
    recipe_instructions: List["str"] = []
    recipe_prep_notes: List["str"] = []

    recipe_cook_time: str = recipe_data["cookTime"]
    recipe_total_time: str = recipe_data["totalTime"]

    # Not sure at the moment what to do with this/what exact data we wanna extract from this
    recipe_yield: str = recipe_data["recipeYield"]


    recipe.set_name(recipe_name)
    print("Recipe Name:", recipe_name)
    print()

    print("Recipe Ingredients: \n")
    for ingredient in recipe_data["recipeIngredient"]:
        recipe_instructions.append(ingredient)
        print(f"  - {ingredient}")
        print()
    print()



    print("Recipe Instructions: \n")
    count = 1
    for instruction in recipe_data["recipeInstructions"]:
        instruction_text: str = instruction["text"]
        if instruction_text == None or instruction_text.startswith("Editor's note:"):
            continue

        if len(instruction_text.split("\nDo Ahead: ")) == 2:
            instr, extra_note = instruction_text.split("\nDo Ahead: ")
            if len(extra_note.split("\n\n")) == 2:
                extra_note, _ = extra_note.split("\n\n")
                recipe_prep_notes.append(extra_note)
            else:
                recipe_prep_notes.append(extra_note)
        # Grab text for each individual instruction
        instruction_text = instruction["text"]
        if instruction_text == None:
            continue

        # Replace measurement abbreviations to facilitate sentence splitting
        instruction_text_lst = instruction_text.split(" ")
        for i in range(len(instruction_text_lst)):
            measurement_category = measurements.get_category(instruction_text_lst[i])
            if measurement_category != "Unknown":
                instruction_text_lst[i] = measurement_category
        
        # print("TEXT: ", instruction_text_lst)

    
        sentences = sent_tokenize(" ".join(instruction_text_lst))
        print("~~~", sentences)
        

        # recipe_instructions.append(instruction_text)
        print(f"{count}) {instruction_text}")
        count += 1

            recipe_instructions.append(instr)
            print(f"{count}) {instr}")
            print()
            continue

        recipe_instructions.append(instruction)
        print(f"{count}) {instruction_text}")
        print()
        count += 1
    print()

    print("Recipe Prep Notes: \n")
    count = 1
    for prep_note in recipe_prep_notes:
        print(f"{count}) {prep_note}")
        count += 1

    print("Recipe Cook Time:", recipe_cook_time)
    print()

    print("Recipe Total Time:", recipe_total_time)
    print()

    print(recipe_yield)
    print()


    # for ingredient in recipe_ingredients:
    #     name, quantity, metric = parse_ingredient(ingredient)
    #     recipe.add_ingredient(name, quantity, metric)

    # for instruction in recipe_instructions:
    #     parsed_instruction = parse_instruction(instruction)
    #     for instruct in parsed_instruction:
    #         recipe.add_instruction(instruct)

    # quantity, metric = parse_time(recipe_cook_time)
    # recipe.add_cook_time(quantity, metric)

    # quantity, metric = parse_time(recipe_total_time)
    # recipe.add_total_time(quantity, metric)


    return recipe
