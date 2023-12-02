
# CS 337 Project 2/2.5 -- RecipeBot
## Collaborators:
- Angeli Mittal
- Javier Cuadra
- Samuel Johnson

## Description
This project is an attempt to mimic LLM chatbots in the form of a recipe reader. When a user runs the main.py file they will be prompted by the chatbot, called the Virtual Chef, to provide a recipe URL of their desired recipe, from there the bot walks the user through the recipe steps while answering clarifying questions along the way. The chatbot was originally developed using recipe links from epicurious.com and works best when provided with URLs from this page.

## Public Github Repository
Link to Repository: [NU-CS337-Angeli-Javi-Sam/Proj-2](https://github.com/NU-CS337-Angeli-Javi-Sam/Proj-2)


## Python Version
v3.10.7

## External Packages Used

- NLTK
- Unicodedata
- BeautifulSoup4

## Set-Up

1. Navigate to the `Proj-2` directory
2. Run the following in Terminal (we are using Python v3.10.7):
   1. `python3 -m venv ./venv`
   2. `source venv/bin/activate`
   3. `pip3 install -r requirements.txt`


## Running Program

1. [Add in instruction to visit page from the web browser, ask Javi about this]
2. Alternatively you may run `python3 main.py` within an IDE of your choice, the main file is what triggers the virtual chef program.

## Interacting with the Chatbot
These are potential commands you can use to interact with the chatbot and inquiry about different aspects of the recipe as you go along:

1. Upon running main.py or accessing the webpage, you will be prompted to enter a recipe URL into the chatbot. After providing a link, the bot will begin to parse the recipe, then it will provide you with 3 options. 

	1. Go over ingredients list
	2. Go over recipe steps
	3. Begin cooking

2. The first one shows all the ingredients for the recipe and the second shows all the recipe steps. Upon selecting the 3rd you begin the recipe loop which starts with the first step of the recipe. From here you can continue to the next step by saying "next" or a similar variant, get a recap of the current step by saying "repeat" or a similar variant, or finally go back to a previous step with "back", "previous" or a similar variant

3. On every you can ask questions about the step and the bot will return a response if applicable. Here is a list of the potential commands:

	1. "Show all ingredients/Show all steps/Show all cooking utensils" or a similar variant will show you all the ingredients, tools or steps of the recipe

	2. "Substitute {recipe variant}" or similar allows you to subsitute the recipe with one of a preselected variants those being halal, kosher, vegetarian, healthy and mexican, which change the recipe ingredients, as well as metric and imperial, which will change the measurements of recipe.
	
	4. Questions about cooking time will give you a response of how long to cook an ingredient for that particular step
	
	5. Questions about temperature and doneness will give you a response about at what temperature to cook an ingredient and/or the visual cues about its doneness level.
	
	6. Questions about what an ingredient is or how to do a certain action will give you a response with a link to a YouTube explaining the action or ingredient.



## Rationale
TBD

### Virtual Chef 
TBD

Perhaps here we can go over a general overview of the parsing of the webpage and handle utterance function calling architecture we used.

### Ontologies
TBD

### Ingredient
TBD

### Instruction
TBD

### Recipe
TBD

### Substitution
TBD
