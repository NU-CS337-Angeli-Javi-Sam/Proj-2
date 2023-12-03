
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

* Navigate to the `Proj-2` directory
* Run the following in Terminal (we are using Python v3.10.7):
   * `python3 -m venv ./venv`
   * `source venv/bin/activate`
   * `pip3 install -r requirements.txt`

## Running Program

* Run `python3 main.py` within a terminal of your choice, the main file is what triggers the virtual chef program.

## Initial Greeting
Upon running `main.py`, you will be prompted to enter a recipe URL into the chatbot. After providing a URL, the bot will begin to parse the recipe before providing you with three options. 

* Go over ingredients list
* Go over recipe steps
* Begin cooking

## Interacting with the Virtual Chef
### Metadata
* If you want to see the ingredients in the entire recipe, provide a command with the phrase "ingredients list" or "all ingredients."
* If you want to see the utensils used in the entire recipe, provide a command with the phrase "all tools" or "all utensils."
* If you want to see the steps for the entire recipe, provide a command with the phrase "all steps."
* If you want to see the name of the recipe, provide a command with the phrase "name of recipe" or "recipe name."

### Navigation
* If you want to go to the next step, provide a command with the phrase "next."
* If you want to go to the previous step, provide a command with the phrase "back" or "previous."
* If you want to go to the repeat the current step, provide a command with the phrase "repeat."
* If you want to go to the nth step, you can utilize one of the following commands:
    * If you provide "go to [n] step" where [n] represents a numeral, you will go to that numbered step. If you provide a numeral that is out of bounds, the program will insult you.
    * If you provide "go to last step," you will go to the last step in the recipe. Alternatively, you could say "what is the last step."
    * If you provide "go to first step," you will go to the first step in the recipe. Alternatively, you could say "what is the first step."

### Transformations/Substitutions
* If you would like to modify the recipe to accommodate a certain diet, you can provide commands with any of the following phrases that begin with "substitute" or "change":
    * "halal"
    * "kosher"
    * "vegetarian"
    * "healthy"
    * "mexican"
* If you would like to modify the recipe to the metric or imperial system, you can provide commands with the phrases "metric" or "imperial," respectively.

### Queries
* If you would like to know what the temperature is for the current step, provide commands with any of the following phrases:
    * "What temperature"
    * "How hot"
    * "How cold"
* If you would like to know the quantity of an ingredient in the current step, provide commands with any one of these phrases, followed by the ingredient in question:
    * "How much"
    * "How many"
* If you would like to know how long a step is quantitatively (i.e., how many minutes the current step will take), then provide commands with the following phrase:
    * "How long"
    *For example, if the step says: "Bring to a low boil on the stovetop over high heat, then reduce heat and simmer (do not boil) until potatoes are very tender when pierced with the tip of a paring knife but not falling apart, 20–25 minutes." Asking "how long" in this case will produce "Do this step for about 20–25 minutes."*
* If you would like to know how long a step is qualitatively (i.e., when to stop doing the current step), provide a command that starts with the word "when."
    * "When" with a step that DOES contain the word "until."
    *For example, if the step says: "Meanwhile, heat 1¼ cup whole milk, 4 thyme sprigs, and ¾ cup (1½ sticks) unsalted butter in a small saucepan over medium, stirring, until butter is melted." Asking "when" in this case will produce "Do this step until butter is melted."*
* If you would like clarification on what something is in the recipe, then you can provide the following phrases, which will direct you to a Google query URL:
    * "What is"
    * "What are"
* If you would like clarification on how to do something in the recipe, then you can provide the following phrases, which will direct you to a YouTube query URL:
    * "How to"
    * "How do"
    * "How should"
**NOTE: If the command includes a pronomial reference that is "this" or "that," then we refer to the current step to create the YouTube query URL.

If the command you provide is invalid for the current step, a generic response will be displayed.

## Rationale
TBD

### Virtual Chef 
Parsing: TBD

Virtual Chef is composed of a central function handle_utterance that takes in user input and using regular expressions determines what the user is asking for or commanding. In the terminal the user will be prompted to provide a recipe URL that then is used to created a Virtual Chef instance to read said recipe. From here the user has the freedom to interact with the Virtual Chef and ask it questions about the recipe as a whole or about the step they are on currently.

The logic breaks down like this, the user gives a command and based on the keywords present in their response the handle_utterance will call a related function to handle that user's request:

handle_navigation_utterance handles commands related to switching between steps, it moves the step pointer up and changes the current instruction text to the next step in the instructions linked list.

handle_meta_utterance handles commands about the recipe as a whole such as "show me all instructions" or "show me all ingredients"

handle_transformation_utterance handles transformation requests to turn recipe into any of the 6 variations we added to the virtual chef. This simply calls the substitute_recipe function in RecipeSubstitutes to create a new recipe using the old recipe virtual chef used to work on. 

Finally, handle_query_utterance handles questions related to a current recipe step and provides answers to inquiries about temperature, how long to cook an item and doneness. This also handles questions about ingredient descriptions or task explanations by providing YouTube links to videos.

### Ontologies
The idea of the ontologies was to give meaning to the most commmon words the bot would encounter in recipes. These ontologies include ingredients, cooking tools, cooking actions, and measurement names. Within each of these ontologies there are dictionaries mapping abstract depictions of tools, actions etc. to their instances for example: "Proteins": "Beef", "Chicken", etc. In Cooking Tools this is done from the tools specialization to tool instance, e.g. "Cutting Tools" : "knife", in Ingredients this is from food group to food, e.g. "Vegetables" : "Carrot", in cooking actions this is done from a action category to action words, e.g. "Heat" : "boil", and finally in measurements this is dictionary of units to their stem variations, e.g. "inch" : "in.", "inches", " " ".

Ontologies further have another dictionary called "lexicon" that reverses the above dictionaries to map the values to the key so given a specific word we can get the category it belongs too. Overall this helps us to find out what words mean in context and how words relate via their category relation.

### Ingredient
Ingredient is the data structure we use to collect meta data about each ingredient used in the recipe. Ingredient contains information about the quantity of an ingredient, the ingredient's full name and simplified name, e.g." Yukon Golden Potatoes" vs "Potatoes", as well as the units used to measurement an ingredient's quantity. This is done by running regular expressions over the raw ingredient text data to extract these features into respectively named fields. 

These objects are collected into a dictionary mentioned below in Recipe object that maps ingredient names to their objects.

### Instruction
Instruction is the data structure we use to collect meta data about each step in the recipe. Instruction allows the virtual chef to answer questions about doneness, temperature, ingredients used in a step as well as the tools and cooking actions used within the step. These are all collected by running a set of regular expressions over the raw instruction text per instruction in the recipe. This allows us to separate things like the ingredients used, temperature, actions and tools into fields of the respective name. For more abstract descriptions of heat or doneness, e.g. "over high heat" or "until golden brown", we save these phrases directly and format them as sentences to be used by the Virutal Chef later on.

These objects are collected into a doubly linked list mentioned below in the Recipe object.

### Recipe
Recipe is a compilation of all relevant recipe items such as tools, ingredients and instructions. When the main.py function is called, it takes the recipe_data dictionary, the URL webpage data in dictionary form, and passes it into the create_recipe function. From here, the recipe_data dictionary's instructions text is broken down into a doubly linked list of instructions, the ingredients text is broken down into a dictionary mapping ingredient names to ingredient objects and finally the tools are stored as a list of tools.

From the recipe is used to create a Virtual Chef that reads the recipe as a it goes to provide the user with the instruction they need to cook with as well as other meta data.

### RecipeSubsitution
Substitution is when we take the ingredients or measurements from the recipe we are currently working on and current it to one of a few variations those being: "healthy", "halal", "kosher", "mexican", "metric", "imperial" or "vegetarian". Based on the selection you chose, the Virtual Chef will called substituteRecipe in RecipeSubstitutions.py which will retrieve the relevant dictionary from the variation and alter the current recipe_data to reflect the change in the ingredients and steps.

For example, if you choose "vegetarian", substituteRecipe will retrieve the vegetarian dictionary which contains substitutions for food items labeled "Proteins" then it changes all the protein ingredients in the recipe_data ingredients and all their occurances in the recipe_data instructions list. The same would be done for "metric" or "imperial", the appropiate dictionary is chosen and all mentions of a unit are switched from metric to imperial or vice versa based on what was mentioned in the recipe_data as well as the measurement number itself. Finally a new recipe is created from the new recipe_data. This new recipe becomes the recipe that Virtual Chef runs.
