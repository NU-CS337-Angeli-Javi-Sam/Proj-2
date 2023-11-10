# from nltk
from typing import List, Union, Dict
from data_structures.ontologies.CookingActions import CookingActionsOntology
from data_structures.ontologies.Ingredients import IngredientOntology
from data_structures.ontologies.CookingTools import CookingToolsOntology
from data_structures.Ingredient import Ingredient
from data_structures.Node import Node
from nltk.stem.snowball import SnowballStemmer
import re

stemmer = SnowballStemmer("english")

# Create Ontology objects
cooking_actions = CookingActionsOntology()
ingredients = IngredientOntology()
tools = CookingToolsOntology()

class Instruction(Node):
    def __init__(self, instruction_sent: str, ingredients: Dict["str", "Ingredient"]) -> None:
        # Give each Instruction __next and __prev variables
        super().__init__()
        self.__instruction = instruction_sent
        self.__tools = self.__set_tools(instruction_sent)
        self.__ingredients = self.__replace_ingredients(self.__set_ingredients(instruction_sent), ingredients)
        self.__cooking_actions = self.__set_cooking_actions(instruction_sent)
        self.__temperature = None
        self.__time = None

    def get_instruction(self):
        return self.__instruction

    def __get_word_stem(self, word: str):
        return stemmer.stem(re.search(r'[A-Za-z]*', word).group(0))

    def __annotate(self, instruction_sent: str, ontology: Union["CookingActionsOntology", "CookingToolsOntology", "IngredientOntology"]):
        word_set = set()
        for word in instruction_sent.split(" "):
            word_stem = self.__get_word_stem(word)
            if ontology.get_category(word_stem) != "Unknown":
                word_set.add(word_stem)
            elif ontology.get_category(word) != "Unknown": # word_stem might be weird
                word_set.add(word)
            elif ontology.get_category(word_stem + 'e') != "Unknown": # word_stem might be weird
                word_set.add(word_stem + 'e')

        word_list = list(word_set)
        return word_list

    def __replace_ingredients(self, ingredient_names: List["str"], ingredients: Dict["str", "Ingredient"]):
        ingredients_set = []
        for ingredient_name in ingredient_names:
            if ingredient_name in ingredients.keys():
                ingredients_set.append(ingredients[ingredient_name])

        return ingredients_set

    def __set_cooking_actions(self, instruction_sent: str) -> None:
        return self.__annotate(instruction_sent, cooking_actions)

    def __set_ingredients(self, instruction_sent: str) -> None:
        return self.__annotate(instruction_sent, ingredients)

    def __set_tools(self, instruction_sent: str) -> None:
        return self.__annotate(instruction_sent, tools)

    def get_cooking_actions(self) -> List["str"]:
        return self.__cooking_actions

    def get_ingredients(self) -> List["str"]:
        return self.__ingredients

    def get_temperature(self) -> str:
        return self.__temperature

    def get_time(self) -> str:
        return self.__time


    def __str__(self) -> str:
        output = f"{self.get_instruction()}\n\n"
        output += f"Cooking Tools: {self.__tools}\n\n"
        output += f"Ingredients: {self.__ingredients}\n\n"
        output += f"Cooking Actions: {self.__cooking_actions}\n\n"

        return output
