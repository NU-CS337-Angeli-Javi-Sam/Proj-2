from nltk.stem.snowball import SnowballStemmer
from data_structures.ontologies.CookingActions import CookingActionsOntology
from data_structures.ontologies.Ingredients import IngredientOntology
from data_structures.ontologies.Measurements import MeasurementsOntology
from data_structures.ontologies.CookingTools import CookingToolsOntology
from nltk.stem.snowball import SnowballStemmer
import re
import unicodedata

stemmer = SnowballStemmer("english")

# Create Ontology objects
cooking_actions = CookingActionsOntology()
ingredients = IngredientOntology()
measurements = MeasurementsOntology()
tools = CookingToolsOntology()

class Ingredient:

    #Representation of ingredient in recipe
    def __init__(self, ingredient_sent):
        self.__original_text = ingredient_sent

        #Name logic
        self.__full_name = None
        self.__simplified_name = None
        self.__qualities = []
        self.__original_text = ingredient_sent

        #Amount logic
        self.__quantity = None
        self.__measurement = []

        self.__set_name(ingredient_sent)
        self.__set_measurement(ingredient_sent)
        self.__set_qualities(ingredient_sent)

    def __get_word_stem(self, word):
        return stemmer.stem(re.search(r'[A-Za-z]*', word).group(0))

    def get_full_name(self):
        return self.__full_name

    def get_original_text(self):
        return self.__original_text

    def get_simplified_name(self):
        return self.__simplified_name

    def get_qualities(self):
        return self.__qualities

    def get_quantity(self):
        return self.__quantity

    def get_measurement(self):
        return self.__measurement

    def __set_name(self, data):
        data = data.replace(',', '').lower().split()

        for index, word in enumerate(data):
            word_stem = self.__get_word_stem(word)

            if ingredients.get_category(word_stem) != "Unknown":
                #Find simple ingredient name
                self.__simplified_name = word
                self.__full_name = word

                #Look for potential adjectives (up to 2 seems to be the norm)
                if index-1 > 0:
                    adj1 = data[index-1]
                    adj1_word_stem = self.__get_word_stem(adj1)

                    if (ingredients.get_category(adj1_word_stem) == measurements.get_category(
                            adj1_word_stem) == tools.get_category(adj1_word_stem) == cooking_actions.get_category(
                            adj1_word_stem)) and not unicodedata.normalize('NFKC', adj1)[0].isdigit():
                        self.__full_name = adj1 + ' ' + self.__full_name

                    if index-2 > 0:
                        adj2 = data[index-2]
                        adj2_word_stem = self.__get_word_stem(adj2)

                        if (ingredients.get_category(adj2_word_stem) == measurements.get_category(
                                adj2_word_stem) == tools.get_category(adj2_word_stem) == cooking_actions.get_category(
                                adj2_word_stem)) and not unicodedata.normalize('NFKC', adj2)[0].isdigit():
                            self.__full_name = adj2 + ' ' + self.__full_name

    def __set_qualities(self, data):
        data = data.replace(',', '').lower().split()

        for word in data:
            word_stem = self.__get_word_stem(word).lower()

            if cooking_actions.get_category(word_stem) != "Unknown":
                self.__qualities.append(word)

    def __set_measurement(self, data):
        data = data.replace(',', '').lower().split()

        for index, word in enumerate(data):
            if unicodedata.normalize('NFKC', word)[0].isdigit():
                if word[-1] == "\"":
                    self.__measurement.append(word[:-1] + ' ' + "inch")
                    continue

                for next_word in data[index:]:
                    if measurements.get_category(next_word) != "Unknown":
                        self.__measurement.append(word + ' ' +  next_word)
                        break
                self.__quantity = word

    def __str__(self):
        return f"Original text: {self.__original_text}\nFull name: {self.__full_name}\nSimplified Name: {self.__simplified_name}\nQualities: {self.__qualities}\nMeasurement: {self.__measurement}\nQuantity: {self.__quantity}\n\n"
