from typing import Dict, Optional
from data_structures.Recipe import Recipe
from data_structures.VirtualChef import VirtualChef
from utils.create_recipe import create_recipe
from utils.fetch_recipe_from_website import fetch_recipe_from_website
from utils.extract_recipe_data import extract_recipe_data


def main() -> None:
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

    # Initializes a Virtual Chef instance that will aid our user in cooking a given recipe
    virtual_chef: VirtualChef = VirtualChef()

    # Recipes to parse
    # ALL RECIPES MUST BE FROM https://www.epicurious.com/
    # url = 'https://www.epicurious.com/recipes/food/views/ba-syn-creamed-spinach-stuffed-meatloaf'
    url: str = "https://www.epicurious.com/recipes/food/views/mashed-potatoes-recipe"
    # url = 'https://www.epicurious.com/recipes/food/views/fresh-cheese-with-spinach-102947'
    # url = "https://www.epicurious.com/recipes/food/views/ba-syn-ropa-vieja"
    # url = "https://www.epicurious.com/recipes/food/views/gulab-jamuns-in-rose-syrup"
    # url = "https://www.epicurious.com/recipes/food/views/blueberry-cobbler"
    # url = "https://www.epicurious.com/recipes/food/views/old-fashioned-235804"

    # Fetch the recipe from the Epicurious website
    recipe_webpage: Optional["str"] = fetch_recipe_from_website(url)

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

    print(recipe)

    # Provide the Virtual Chef the recipe to use
    virtual_chef.set_recipe(recipe)


if __name__ == "__main__":
    main()
