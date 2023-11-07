from data_structures.VirtualChef import VirtualChef
from parsers.parse_instruction import parse_instruction
from utils.create_recipe import create_recipe
from utils.fetch_recipe import fetch_recipe
from utils.html_parser import parse_html

def main():
    # Takes in recipe
    virtual_chef = VirtualChef()

    # Recipe to parse
    # url = 'https://www.epicurious.com/recipes/food/views/ba-syn-creamed-spinach-stuffed-meatloaf'
    # url = 'https://www.epicurious.com/recipes/food/views/my-favorite-simple-roast-chicken-231348'
    url = 'https://www.epicurious.com/recipes/food/views/mashed-potatoes-recipe'

    # Do surface-level parsing of HTML
    webpage_content = fetch_recipe(url)
    parsed_html = parse_html(webpage_content)

    # for key in parsed_html:
    #     print(key)
    #     print()

    # Compartmentalizes components of recipe given parsed HTML into a Recipe object
    recipe = create_recipe(parsed_html)

    # Create annotations for each step


    # virtual_chef.set_recipe(recipe)

    # sentence = 'chop onions with knife'
    # print(parse_instruction(sentence))

if __name__ == "__main__":
    main()
    