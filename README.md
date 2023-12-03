
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

1. Run `python3 main.py` within a terminal of your choice, the main file is what triggers the virtual chef program.

## Interacting with the Chatbot
These are potential commands you can use to interact with the chatbot and inquiry about different aspects of the recipe as you go along:

1. Upon running main.py, you will be prompted to enter a recipe URL into the chatbot. After providing a URL, the bot will begin to parse the recipe before providing you with three options. 

	1. Go over ingredients list
	2. Go over recipe steps
	3. Begin cooking

2. The first one shows all the ingredients for the recipe and the second shows all the recipe steps. Upon selecting the third you begin the Virtual Chef program (which starts with the first step of the recipe). From here, you can continue to the next step by saying some phrase that contains the word "next." You can also get a recap of the current step by giving a phrase that includes "repeat." You can also go back to a previous step by saying a phrase that either contains "back." Keep in mind: Any sentence that includes these keywords will follow these rules (thus, don't include these keywords unless you want to do these navigations). We did not include the ability to finish in the middle of the recipe; you can only finish by saying "next" on the last step.

3. On every step you can ask questions about the step, and the bot will return a response, if applicable. Here is a list of the potential commands:

	1. "Show all ingredients," "Show all steps," or "Show all cooking utensils"/"Show all cooking tools" will show you all the ingredients, steps, or utensils of the recipe, respectively.

	2. "Substitute {recipe variant}" allows you to subsitute the recipe with one of a preselected variants. These are: halal, kosher, vegetarian, healthy, and mexican. These will change the recipe ingredients, as well as metric and imperial units, which will change the measurements of recipe.
	
	4. Questions about cooking time will give you a response of how long to cook an ingredient for that particular step. If the step includes a duration of time, then by asking the Virtual Chef containing the keyword "how long" will give you that duration of time. For example, if the step says: "Bring to a low boil on the stovetop over high heat, then reduce heat and simmer (do not boil) until potatoes are very tender when pierced with the tip of a paring knife but not falling apart, 20–25 minutes." Asking "how long" in this case will produce "Do this step for about 20–25 minutes." 
	
	5. If the step includes the word "until," then by asking Virtual Chef a question containing the keyword "when" will give you a qualitative response of when the step would be done. For example, a step may be "Meanwhile, heat 1¼ cup whole milk, 4 thyme sprigs, and ¾ cup (1½ sticks) unsalted butter in a small saucepan over medium, stirring, until butter is melted." Asking "when" in this case will produce "Do this step until butter is melted."
	
	6. Questions about temperature and doneness will give you a response about at what temperature to cook an ingredient and/or the visual cues about its doneness level.

 	7. Questions about what an ingredient is or how to do a certain action will give you a response with a link to a YouTube explaining the action or ingredient.

## Rationale
TBD

### Virtual Chef 
Parsing: TBD

Virtual Chef is composed of a central function handle_utterance that takes in user input and using regular expressions determines what the user is asking for or commanding. In the terminal the user will be prompted to provide a recipe URL that then is used to created a Virtual Chef instance to read said recipe. From here the user has the freedom to interact with the Virtual Chef and ask it questions about the recipe as a whole or about the step they are on currently.

The logic breaks down like this, the user gives a command and based on the keywords present in their response the handle_utterance will call a related function to handle that user's request:

handle_navigation_utterance handles commands related to switching between steps, it moves the step pointer up and changes the current instruction text to the next step in the instructions linked list.

handle_meta_utterance handles commands about the recipe as a whole such as "show me all instructions" or "show me all ingredients

handle_transformation_utterance handles transformation requests to turn recipe into any of the 6 variations we added to the virtual chef. This simply calls the substitute_recipe function in RecipeSubstitutes to create a new recipe using the old recipe virtual chef used to work on. 

Finally, handle_query_utterance handles questions related to a current recipe step and provides answers to inquiries about temperature, how long to cook an item and doneness. This also handles questions about ingredient descriptions or task explanations by providing YouTube links to videos.

### Ontologies
The idea of the ontologies was to give meaning to the most commmon words the bot would encounter in recipes. These ontologies include ingredients, cooking tools, cooking actions, and measurement names. Within each of these ontologies there are dictionaries mapping abstract depictions of tools, actions etc. to their instances for example: "Proteins": "Beef", "Chicken", etc. In Cooking Tools this is done from the tools specialization to tool instance, e.g. "Cutting Tools" : "knife", in Ingredients this is from food group to food, e.g. "Vegetables" : "Carrot", in cooking actions this is done from a action category to action words, e.g. "Heat" : "boil", and finally in measurements this is dictionary of units to their stem variations, e.g. "inch" : "in.", "inches", " " ".

Ontologies further have another dictionary called "lexicon" that reverses the above dictionaries to map the values to the key so given a specific word we can get the category it belongs too. Overall this helps us to find out what words mean in context and how words relate via their category relation.

### Ingredient
TBD

### Instruction
TBD

### Recipe
Recipe is a compilation of all relevant recipe items such as tools, ingredients and instructions. When the main.py function is called, it takes the recipe_data dictionary, the URL webpage data in dictionary form, and passes it into the create_recipe function. From here, the recipe_data dictionary's instructions text is broken down into a doubly linked list of instructions, the ingredients text is broken down into a dictionary mapping ingredient names to ingredient objects and finally the tools are stored as a list of tools.

From the recipe is used to create a Virtual Chef that reads the recipe as a it goes to provide the user with the instruction they need to cook with as well as other meta data.

### RecipeSubsitution
Substitution is when we take the ingredients or measurements from the recipe we are currently working on and current it to one of a few variations those being: "healthy", "halal", "kosher", "mexican", "metric", "imperial" or "vegetarian". Based on the selection you chose, the Virtual Chef will called substituteRecipe in RecipeSubstitutions.py which will retrieve the relevant dictionary from the variation and alter the current recipe_data to reflect the change in the ingredients and steps.

For example, if you choose "vegetarian", substituteRecipe will retrieve the vegetarian dictionary which contains substitutions for food items labeled "Proteins" then it changes all the protein ingredients in the recipe_data ingredients and all their occurances in the recipe_data instructions list. The same would be done for "metric" or "imperial", the appropiate dictionary is chosen and all mentions of a unit are switched from metric to imperial or vice versa based on what was mentioned in the recipe_data as well as the measurement number itself. Finally a new recipe is created from the new recipe_data. This new recipe becomes the recipe that Virtual Chef runs.
