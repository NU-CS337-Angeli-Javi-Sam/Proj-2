# from nltk
from data_structures.ontologies.CookingActions import CookingActionsOntology
from data_structures.ontologies.Ingredients import IngredientOntology
from data_structures.ontologies.CookingTools import CookingToolsOntology
from data_structures.Node import Node
from nltk.stem.snowball import SnowballStemmer
import re

stemmer = SnowballStemmer("english")

# Create Ontology objects
cooking_actions = CookingActionsOntology()
ingredients = IngredientOntology()
tools = CookingToolsOntology()

class Instruction(Node):
    def __init__(self, instruction_sent):
        # Give each Instruction __next and __prev variables
        super().__init__()

        self.__instruction = instruction_sent
        self.__tools = []
        self.__ingredients = []
        self.__cooking_actions = []
        self.__temperature = None
        self.__time = None

        # Set variables
        print(instruction_sent)
        self.__set_cooking_actions(instruction_sent)
        self.__set_ingredients(instruction_sent)
        self.__set_tools(instruction_sent)

    def get_instruction(self):
        return self.__instruction

    def __get_word_stem(self, word):
        return stemmer.stem(re.search(r'[A-Za-z]*', word).group(0))

    def __annotate(self, instruction_sent, ontology, variable):
        for word in instruction_sent.split(" "):
            word_stem = self.__get_word_stem(word)
            if ontology.get_category(word_stem) != "Unknown":
                variable.append(word_stem)

        variable = list(set(variable))

    def __set_cooking_actions(self, instruction_sent):
        self.__annotate(instruction_sent, cooking_actions, self.__cooking_actions)

    def __set_ingredients(self, instruction_sent):
        self.__annotate(instruction_sent, ingredients, self.__ingredients)

    def __set_tools(self, instruction_sent):
        self.__annotate(instruction_sent, tools, self.__tools)

    def get_cooking_actions(self):
        return self.__cooking_actions

    def get_ingredients(self):
        return self.__ingredients

    def __str__(self):
        return f"Cooking Tools: {self.__tools}\nIngredients: {self.__ingredients}\nCooking Actions: {self.__cooking_actions}\n\n"
