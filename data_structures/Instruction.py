# from nltk
from data_structures.ontologies.CookingActions import CookingActionsOntology
from data_structures.Node import Node
from nltk.stem.snowball import SnowballStemmer
import re

stemmer = SnowballStemmer("english")
cooking_actions = CookingActionsOntology()

class Instruction(Node):
    def __init__(self, instruction_sent):
        # Give each Instruction __next and __prev variables
        super().__init__()

        self.__utensils = []
        self.__ingredients = []
        self.__cooking_actions = []
        self.__temperature = None
        self.__time = None

        # Set variables
        print(instruction_sent)
        self.__set_cooking_actions(instruction_sent)

    def __set_cooking_actions(self, instruction_sent):
        for word in instruction_sent.split(" "):
            word_stem = stemmer.stem(re.search(r'[A-Za-z]*', word).group(0))
            if cooking_actions.get_category(word_stem) != "Unknown":
                self.__cooking_actions.append(word_stem)

    def get_cooking_actions(self):
        return self.__cooking_actions

    def __str__(self):
        return f"Utensils: {self.__utensils}\nIngredients: {self.__ingredients}\nCooking Actions: {self.__cooking_actions}\n\n"