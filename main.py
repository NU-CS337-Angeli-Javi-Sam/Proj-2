import requests

from data_structures.DoublyLinkedList import DoublyLinkedList

# URL of the webpage
# url = 'https://www.epicurious.com/recipes/food/views/ba-syn-creamed-spinach-stuffed-meatloaf'
# url = 'https://www.foodnetwork.com/recipes/food-network-kitchen/salad-stuffed-peppers-9970168'

# # Send an HTTP GET request to the URL
# response = requests.get(url)

# if response.status_code == 200:
#     # Get the webpage content
#     webpage_content = response.text

#     # Save the content to a file
#     with open('webpage_content1.html', 'w', encoding='utf-8') as file:
#         file.write(webpage_content)

#     print(f"Webpage content has been saved to 'webpage_content.html'.")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    dll = DoublyLinkedList()
