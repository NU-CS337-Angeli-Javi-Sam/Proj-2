
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
For this project, we created a dependency parser (in line with the class suggestions) with the intent of using its output to create relevant objects and ontologies. However, we found out we could achieve similar results by re-implementing regex expressions similar to the first project. Therefore, our project uses regex expressions to perform the parsing of our recipes. Once our recipe has been parsed, we re-utilized regex expressions to identify commands the user wants to perform based on their utterances. After identifying which command the user provided, we use a set of handlers to give relevant responses to the user. This is the overall approach we took when implementing this program.


in an object-oriented form of language processor. We created regex expressions (similar to project 1) to 



 We did not end of using the dependency parser because by using simple r

### Initializing and Interacting with Virtual Chef
Virtual Chef is composed of a central function `handle_utterance` that takes in user input and using regular expressions determines what the user is asking for or commanding. In the terminal, the user will be prompted to provide a recipe URL that is then used to create a Virtual Chef instance that parses said recipe. 

The recipes that can be provided are from the Epicurious website, which already formats its website such that scraping is not necessary. Instead, we grab the important information in the HTML code within the `recipe_data` object provided to the `create_recipe` function (see next section). For example, we grab the recipe ingredients and recipe steps. Using various ontologies (see next section), we determined what the actual ingredients, tools, cooking actions, measurements, and recipe substitutions were based on the ingredients and steps provided in the HTML code. We then used a recipe relationships ontology to tie the various cooking actions to tools and ingredients. During this process, we also created an `Ingredient` class that provided more specifications based on the qualities described in the HTML. We similarly did this for instructions, creating an `Instruction` class.

Once all of the parsing was complete, the user has the freedom to interact with the Virtual Chef and ask it questions about the recipe as a whole or about the step they are on currently.

Based on the user's command, we will call one of the following helper functions:
* `handle_navigation_utterance` handles commands related to step navigation by the step pointer in our doubly-linked list.
* `handle_meta_utterance` handles commands about the recipe as a whole, such as "show me all instructions" or "show me all ingredients."
* `handle_transformation_utterance` handles requests to transform the recipe into any of the six variations programmed into the Virtual Chef. This handler calls the `substitute_recipe` function in `RecipeSubstitutes` to create a new recipe using the old recipe Virtual Chef used to work on. 
* `handle_query_utterance` handles queries related to the current recipe step, such as temperature, duration, and doneness. This handler also generates queries for YouTube or Google based on user's commands, if applicable.

### Ontologies
The idea of the ontologies was to give meaning to the most commmon words the bot would encounter in recipes. These ontologies include ingredients, cooking tools, cooking actions, and measurement names. Within each of these ontologies, there are dictionaries mapping abstract depictions of tools, actions, ingredients, measurements, and substitutions. For example, in the `Ingredients` ontology, there are categories such as "proteins," which has values like "beef" and "chicken."

Ontologies have another dictionary called `lexicon` that maps the ontologies' category values to category names. For example, if the `lexicon` contains the word "chicken," then the values will be mapped to "protein." Overall this helps us to find out what words mean in context and how words relate via their category relation.

### Ingredient
`Ingredient` is an object that stores the original text, full name (provided in the HTML), a simplified name without the extra descriptors (e.g. Yukon Gold potatoes will be turned into potatoes), a quantity (if provided), and qualities (if provided). We use these extra descriptors for the queries a user might give.

### Instruction
`Instructions` are a representation of nodes in the doubly-linked list that holds all of the instructions. It contains the full text of the recipe instruction, the tools used in this instruction, the ingredients used in this instruction, the cooking action performed in the instruction, the temperature at which this instruction is performed (if applicable), the duration at which this instruction is performed (if applicable), and finally, the done criterion at which this instruction is deemed completed (if applicable). We use these criteria to answer user queries regarding the instructions. 

### Recipe
`Recipe` is an object that stores the name, ingredients, instructions, and tools used in the recipe. It is created after providing the URL and retrieving the HTML from Epicurious. The instructions are stored within a doubly-linked list, and the ingredients are in a dictionary (where the keys are the simplified name, if available). We then set the recipe within the Virtual Chef to be the `Recipe` object.

### RecipeSubsitutions
We have a pre-selected list of recipe substitutions (e.g., "healthy," "halal", "kosher", "mexican", "metric", "imperial" or "vegetarian"). Based on the selection you chose, the Virtual Chef will call `substituteRecipe` in `RecipeSubstitutions.py` which will retrieve the relevant dictionary from the variation and alter the current `recipe_data` to reflect the change in the ingredients and steps.

For example, if you choose "vegetarian", `substituteRecipe` will retrieve the vegetarian dictionary, which contains substitutions for food items labeled "Proteins," then it changes all the protein ingredients in the `recipe_data` ingredients and all its occurrances in the `recipe_data` instructions list. Finally a new recipe is created from the new `recipe_data.` This new recipe becomes the recipe that Virtual Chef runs.
