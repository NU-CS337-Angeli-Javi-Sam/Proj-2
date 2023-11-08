import json
from typing import Dict, Optional
from bs4 import BeautifulSoup, Tag


def extract_recipe_data(html_content: str) -> Optional["Dict"]:
    """
    Extracts recipe data from HTML content using JSON-LD markup.

    This function parses the HTML content using BeautifulSoup and extracts recipe-related data
    from a JSON-LD script tag commonly used in webpages to provide structured data.

    Parameters:
    - html_content (str): The HTML content of the webpage.

    Returns:
    - dict: A Python dictionary containing recipe data, as structured in the JSON-LD markup.

    Example:
    >>> webpage_content = "<html>...</html>"  # Replace with the actual HTML content
    >>> recipe_data = extract_recipe_data(webpage_content)
    >>> if recipe_data:
    >>>     print("Recipe data:", recipe_data)
    >>> else:
    >>>     print("Failed to extract recipe data from the HTML content.")
    """

    soup: BeautifulSoup = BeautifulSoup(html_content, "html.parser")
    script_tag: Optional["Tag"] = soup.find("script", type="application/ld+json")
    json_content: Optional["str"] = script_tag.string if script_tag else None
    recipe_data: Optional["Dict"] = json.loads(json_content) if json_content else None

    return
