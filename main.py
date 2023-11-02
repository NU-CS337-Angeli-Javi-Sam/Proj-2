from utils.fetch_recipe import fetch_recipe
from utils.html_parser import parse_html

if __name__ == "__main__":
    # url = 'https://www.epicurious.com/recipes/food/views/ba-syn-creamed-spinach-stuffed-meatloaf'
    # url = 'https://www.epicurious.com/recipes/food/views/my-favorite-simple-roast-chicken-231348'
    url = 'https://www.epicurious.com/recipes/food/views/mashed-potatoes-recipe'

    webpage_content = fetch_recipe(url)

    parsed_html = parse_html(webpage_content)

    recipe_ingredients = parsed_html["recipeIngredient"]
    recipe_instructions = parsed_html["recipeInstructions"]

    print()
    for ingredient in recipe_ingredients:
        print(ingredient)

    print()

    for instruction in recipe_instructions:
        print(instruction["text"])
        print("--")
