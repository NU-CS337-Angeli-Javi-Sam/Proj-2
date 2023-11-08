from typing import Optional
from requests import Request, Response

def fetch_recipe_from_website(url: str) -> Optional["str"]:
    """
    Fetches the content of a recipe webpage from a given URL.

    This function sends an HTTP GET request to the specified URL and retrieves the webpage content.

    Parameters:
    - url (str): The URL of the webpage containing the recipe.

    Returns:
    - Optional[str]: The webpage content as a string, or None if the request fails.

    Example:
    >>> recipe_url = "https://www.example.com/recipes/spaghetti"
    >>> recipe_content = fetch_recipe_from_website(recipe_url)
    >>> if recipe_content:
    >>>     print("Recipe content:", recipe_content)
    >>> else:
    >>>     print("Failed to retrieve the recipe page.")
    """

    response: Response = Request.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    # Get the webpage content
    webpage_content: str = response.text
    return webpage_content
