from typing import Any, Dict, List, Tuple
from nltk.tokenize import sent_tokenize

from data_structures.Recipe import Recipe
from data_structures.Instruction import Instruction
from data_structures.Ingredient import Ingredient
from data_structures.ontologies.Measurements import MeasurementsOntology

# nltk.download('punkt')
measurements = MeasurementsOntology()

def create_recipe_ingredients_dict(
    recipe_ingredients: List["str"],
) -> Dict["str", "Ingredient"]:
    """
    Creates a dictionary of ingredients for a recipe.

    Given a list of strings representing recipe ingredients, this function processes and parses each ingredient
    into an Ingredient object and populates a dictionary, associating the ingredient string with its Ingredient object.

    Parameters:
    - recipe_ingredients (List[str]): A list of strings representing recipe ingredients.

    Returns:
    - Dict[str, Ingredient]: A dictionary where each key is the string representation of the ingredient, and the value
      is the corresponding Ingredient object.
    """

    recipe_ingredients_dict: Dict["str", "Ingredient"] = {}

    for ingredient in recipe_ingredients:
        if "Special Equipment" in ingredient:
            continue

        ingredient_sentence: str = replace_abbreviations(ingredient)

        ingredient_sentence_tokens = sent_tokenize(ingredient_sentence)[0]

        parsed_ingredient: Ingredient = Ingredient(ingredient_sentence_tokens)

        if parsed_ingredient.get_simplified_name():
            recipe_ingredients_dict[parsed_ingredient.get_simplified_name()] = parsed_ingredient
        else:
            recipe_ingredients_dict[parsed_ingredient.get_original_text()] = parsed_ingredient


    return recipe_ingredients_dict


def replace_abbreviations(ingredient_sentence: str) -> str:
    """
    Replaces abbreviations in an ingredient sentence with their full measurement terms.

    This function takes an ingredient sentence and identifies any measurement abbreviations within it.
    It replaces these abbreviations with their full measurement terms.

    Parameters:
    - ingredient_sentence (str): A string representing the ingredient sentence.

    Returns:
    - str: The updated ingredient sentence with full measurement terms replacing any abbreviations.
    """

    ingredient_sentence_lst: List["str"] = ingredient_sentence.split(" ")

    for i in range(len(ingredient_sentence_lst)):
        measurement: str = measurements.get_category(ingredient_sentence_lst[i])

        if measurement != "Unknown":
            ingredient_sentence_lst[i] = measurement

    updated_ingredient_sentence: str = " ".join(ingredient_sentence_lst)

    return updated_ingredient_sentence


def get_and_set_recipe_name(recipe: Recipe, recipe_data: Any) -> None:
    """
    Retrieves and sets the name of a recipe.

    Extracts the name of the recipe from the provided recipe data and sets it in the Recipe object.

    Parameters:
    - recipe (Recipe): The Recipe object to update.
    - recipe_data (Any): Any data structure representing the recipe details.
    """

    recipe_name: str = recipe_data["name"]

    recipe.set_name(recipe_name)


def get_and_set_recipe_ingredients(recipe: Recipe, recipe_data: Any) -> None:
    """
    Retrieves and sets the ingredients of a recipe.

    Extracts the recipe ingredients from the provided recipe data, processes, and parses each ingredient into
    an Ingredient object. It creates a dictionary with the string representation of the ingredient as the key
    and the corresponding Ingredient object as the value. These ingredients are added to the Recipe object.

    Parameters:
    - recipe (Recipe): The Recipe object to update.
    - recipe_data (Any): Any data structure representing the recipe details.
    """
    recipe_ingredients: List["str"] = []

    for ingredient in recipe_data["recipeIngredient"]:
        recipe_ingredients.append(ingredient)

    recipe_ingredients_dict: Dict["str", "Ingredient"] = create_recipe_ingredients_dict(
        recipe_ingredients
    )

    recipe.add_ingredients(recipe_ingredients_dict)


def replace_ingredients(
    recipe_ingredients: Dict["str", "Ingredient"], instruction_text: str
) -> str:
    """
    Replace ingredient names in instruction text with simplified names.

    Given a dictionary of recipe ingredients and an instruction text, this function replaces occurrences of full ingredient
    names in the instruction text with their simplified names, making the text more user-friendly and easier to read.

    Parameters:
    - recipe_ingredients (Dict[str, Ingredient]): A dictionary of recipe ingredients where keys are full ingredient names,
      and values are Ingredient objects.
    - instruction_text (str): The original instruction text.

    Returns:
    - str: The updated instruction text with full ingredient names replaced by their simplified names.
    """
    updated_text: str = instruction_text

    for ingredient_name, ingredient in recipe_ingredients.items():
        ingredient_simplified_name: str = ingredient.get_simplified_name()

        updated_text: str = updated_text.replace(
            ingredient_name, ingredient_simplified_name
        )

    return updated_text


def parse_recipe_instruction(
    recipe: Recipe, instructions: List["str"]
) -> Tuple[List["str"], List["str"]]:
    """
    Parse and process recipe instructions.

    Given a Recipe object and a list of instruction strings, this function parses each instruction, handling any special
    sections like "Do Ahead," and replaces ingredient names with their simplified names. It also separates preparation notes.

    Parameters:
    - recipe (Recipe): The Recipe object to update with the parsed instructions.
    - instructions (List[str]): A list of instruction strings from the recipe data.

    Returns:
    - Tuple[List[str], List[str]]: A tuple containing two lists - the parsed recipe instructions and any preparation notes.
    """

    recipe_instructions: List["Instruction"] = []
    recipe_prep_notes: List["str"] = []
    recipe_ingredients: Dict["str", "Ingredient"] = recipe.get_ingredients()

    for instruction in instructions:
        # Grab text for each individual instruction
        instruction_text: str = instruction["text"]

        # Handle "Do Ahead:" in instructions
        if len(instruction_text.split("\nDo Ahead: ")) == 2:
            instruction_text, extra_note = instruction_text.split("\nDo Ahead: ")

            # Remove Editor's note
            if len(extra_note.split("\n\nEditor's note: ")) == 2:
                extra_note, _ = extra_note.split("\n\n")
                recipe_prep_notes.append(extra_note)
            elif len(extra_note.split("\n\nEditor’s note: ")) == 2:
                extra_note, _ = extra_note.split("\n\n")
                recipe_prep_notes.append(extra_note)
            else:
                recipe_prep_notes.append(extra_note)



        if len(instruction_text.split("\n\nEditor’s note: ")) == 2:

            instruction_text, _ = instruction_text.split("\n\nEditor’s note: ")
        elif len(instruction_text.split("\n\nEditor's note: ")) == 2:

            instruction_text, _ = instruction_text.split("\n\nEditor's note: ")




        instruction_text = replace_abbreviations(instruction_text)

        # instruction_text = replace_ingredients(recipe_ingredients, instruction_text)

        sentences: List["str"] = sent_tokenize(instruction_text)

        for sentence in sentences:
            new_instruction: Instruction = Instruction(sentence, recipe.get_ingredients())
            recipe_instructions.append(new_instruction)

    return recipe_instructions, recipe_prep_notes


def get_and_set_recipe_instructions(recipe: Recipe, recipe_data: Any) -> None:
    """
    Retrieve and set the recipe instructions in a Recipe object.

    Extracts the recipe instructions from the provided recipe data, processes and parses them, and adds them to the Recipe
    object. Any preparation notes are separated and stored in the Recipe object.

    Parameters:
    - recipe (Recipe): The Recipe object to update with instructions.
    - recipe_data (Any): Any data structure representing the recipe details, including instructions.
    """

    instructions: List["str"] = recipe_data["recipeInstructions"]

    recipe_instructions, recipe_prep_notes = parse_recipe_instruction(
        recipe, instructions
    )

    recipe.add_instructions(recipe_instructions)

    recipe.add_tools()


def get_and_set_recipe_cook_time(recipe: Recipe, recipe_data: Any) -> None:
    # recipe_cook_time: str = recipe_data["cookTime"]
    pass

def get_and_set_recipe_total_time(recipe: Recipe, recipe_data: Any) -> None:
    # recipe_total_time: str = recipe_data["totalTime"]
    pass

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
