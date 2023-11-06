from typing import List
from data_structures.Recipe import Recipe
from parsers.parse_ingredient import parse_ingredient
from parsers.parse_instruction import parse_instruction
from parsers.parse_time import parse_time


def create_recipe(recipe_data):
    recipe: Recipe = Recipe()

    recipe_name: str = recipe_data["name"]
    recipe_ingredients: List["str"] = recipe_data["recipeIngredient"]
    recipe_instructions: List["str"] = []


    recipe_cook_time: str = recipe_data["cookTime"]
    recipe_total_time: str = recipe_data["totalTime"]

    # Not sure at the moment what to do with this/what exact data we wanna extract from this
    recipe_yield: str = recipe_data["recipeYield"]


    recipe.set_name(recipe_name)
    print("Recipe: ", recipe_name)
    print()

    print("Recipe Ingredients: ", recipe_ingredients)
    print()

    print("Recipe:")
    count = 1
    for instruction in recipe_data["recipeInstructions"]:
        instruction_text = instruction["text"]
        if instruction_text == None:
            continue

        recipe_instructions.append(instruction_text)
        print(f"{count}) {instruction_text}")
        count += 1

    print("Recipe Cook Time: ", recipe_cook_time)
    print()

    print("Recipe Total Time: ", recipe_total_time)
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
