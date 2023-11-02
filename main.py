from data_structures.VirtualChef import VirtualChef
from utils.create_recipe import create_recipe
from utils.fetch_recipe import fetch_recipe
from utils.html_parser import parse_html

if __name__ == "__main__":
    virtual_chef = VirtualChef()

    # url = 'https://www.epicurious.com/recipes/food/views/ba-syn-creamed-spinach-stuffed-meatloaf'
    # url = 'https://www.epicurious.com/recipes/food/views/my-favorite-simple-roast-chicken-231348'
    url = 'https://www.epicurious.com/recipes/food/views/mashed-potatoes-recipe'

    webpage_content = fetch_recipe(url)

    parsed_html = parse_html(webpage_content)

    for key in parsed_html:
        print(key)
        print()

    recipe = create_recipe(parsed_html)

    virtual_chef.set_recipe(recipe)
