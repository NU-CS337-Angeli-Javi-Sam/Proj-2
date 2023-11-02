import requests


def fetch_recipe(url):
    response = requests.get(url)

    if response.status_code == 200:
        # Get the webpage content
        webpage_content = response.text
        return webpage_content

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
