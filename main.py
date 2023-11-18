from typing import Dict, Optional
from data_structures.Instruction import Instruction
from data_structures.Recipe import Recipe
from data_structures.VirtualChef import VirtualChef
from utils.create_recipe import create_recipe
from utils.fetch_recipe_from_website import fetch_recipe_from_website
from utils.extract_recipe_data import extract_recipe_data

def initialize_virtual_chef() -> None:
    virtual_chef: VirtualChef = VirtualChef()
    return virtual_chef

def prompt_user_for_recipe() -> None:
    print("Welcome to Virtual Chef, my culinary companion! I'm here to turn your kitchen into a playground of flavors. I'm Virtual Chef, and together, we're going to cook up a storm.\n")
    print("Now, before we dive into the world of gastronomic wonders, I need you to do something for me. Don't worry, it's not as stressful as a dinner service at Hell's Kitchen – I promise. I want you to share with me a recipe URL. Give me the dish you've been craving, and let's bring it to life in your kitchen. Keep in mind, we need this recipe to be from Epicurious; otherwise, we cannot proceed.\n")
    print("So, go ahead and toss me that link. Whether it's a family secret or a culinary challenge, I'm ready to take it on. Let's get cooking!\n")

    recipe_url = input("> Recipe URL: ")

    print("\nGive me a moment to fetch this recipe.\n")

    return recipe_url

def process_recipe(virtual_chef: VirtualChef, recipe_url: str) -> None:
    """
    The main function to extract and process a recipe from a specific website.

    This function orchestrates the entire process of fetching a recipe from a website,
    extracting relevant data, and creating a Recipe object to be used by a Virtual Chef.

    It follows the following steps:
    1. Initializes a Virtual Chef instance to assist the user in cooking a recipe.
    2. Specifies the URL of the recipe webpage to be fetched.
    3. Fetches the HTML content of the webpage using the specified URL.
    4. Extracts relevant recipe data from the HTML content.
    5. Creates a Recipe object from the extracted recipe data.
    6. Provides the Virtual Chef with the created Recipe object.

    Example:
    - Replace the 'url' variable with the URL of the desired recipe.
    - Execute the 'main' function to fetch, extract, and process the recipe.
    """


    # Recipes to parse
    # ALL RECIPES MUST BE FROM https://www.epicurious.com/
    # url = 'https://www.epicurious.com/recipes/food/views/ba-syn-creamed-spinach-stuffed-meatloaf'
    # url: str = "https://www.epicurious.com/recipes/food/views/mashed-potatoes-recipe"
    # url = 'https://www.epicurious.com/recipes/food/views/fresh-cheese-with-spinach-102947'
    # url = "https://www.epicurious.com/recipes/food/views/ba-syn-ropa-vieja"
    # url = "https://www.epicurious.com/recipes/food/views/gulab-jamuns-in-rose-syrup"
    # url = "https://www.epicurious.com/recipes/food/views/blueberry-cobbler"
    # url = "https://www.epicurious.com/recipes/food/views/old-fashioned-235804"

    # Fetch the recipe from the Epicurious website
    recipe_webpage: Optional["str"] = fetch_recipe_from_website(recipe_url)

    if recipe_webpage == None:
        print("Something went wrong when fetching the webpage. Try again.")
        return

    # Extract relevant data from HTML
    recipe_data: Optional["Dict"] = extract_recipe_data(recipe_webpage)

    if recipe_data == None:
        print("Something went wrong when parsing the HTML. Try again.")
        return

    # Creates a Recipe object from the provided recipe data
    recipe: Recipe = create_recipe(recipe_data)

    # print(recipe)

    # Provide the Virtual Chef the recipe to use
    virtual_chef.set_recipe(recipe)

def prompt_user_to_begin(virtual_chef: VirtualChef) -> None:
    recipe_name: str = virtual_chef.get_recipe().get_name()
    print(f"Ah, fantastic choice with {recipe_name}! Now, we're standing at the crossroads of culinary delight. Do you want to dive straight into the action and begin cooking, or would you prefer to review the ingredients first? The stage is set, and the choice is yours. Let me know, and we'll make this kitchen dance truly memorable!\n")
    print("[1] Go over ingredients list")
    print("[2] Go over recipe steps\n")

    response = input("> Command: ")
    return response

def begin_cooking(virtual_chef: VirtualChef) -> None:
    recipe_name: str = virtual_chef.get_recipe().get_name()
    print(f"\nGreat decision! We're not wasting any time. Now, let's roll up those sleeves and get started on this {recipe_name} adventure.\n")
    curr_instruction: Instruction = virtual_chef.get_next_instruction()

    print(f"First step: {curr_instruction.get_instruction()}\n")

    while True:
        user_input: str = input("> ")

        response: str = virtual_chef.handle_utterance(user_input)

        if response == "break":
            break

        print(f"\n{response}\n")


def finish_cooking(virtual_chef: VirtualChef) -> None:
    recipe_name: str = virtual_chef.get_recipe().get_name()

    print(f"Bravo! You've conquered the first leg of our {recipe_name} expedition. I can almost smell the incredible aromas wafting from your kitchen. Now, take a moment to appreciate your culinary masterpiece.\n")

    print("As we stand here with our finished dish, the real question is, how does it taste? Is it a symphony of flavors dancing on your taste buds, or does it need a little touch-up? Let me know how it turned out, and if you have any questions or if there's another culinary escapade you'd like to embark on. I'm here to guide you through the world of flavors. Well done, chef!")


def main():
    virtual_chef: VirtualChef = initialize_virtual_chef()
    recipe_url: str = prompt_user_for_recipe()
    process_recipe(virtual_chef, recipe_url)
    print(virtual_chef.get_recipe())
    response: str = prompt_user_to_begin(virtual_chef)

    while True:
        if response.isnumeric() and int(response) == 1:
            all_ingredients: str = virtual_chef.get_all_ingredients()
            print(all_ingredients)
        elif response.isnumeric() and int(response) == 2:
            break
        else:
            print("\n\nPlease input 1 or 2 corresponding to the following commands.")

        print("\nPlease provide your input:\n")
        print("[1] Go over ingredients list")
        print("[2] Go over recipe steps.\n")
        response: int = input("> Command: ")

    begin_cooking(virtual_chef)

    finish_cooking(virtual_chef)

if __name__ == "__main__":
    main()
