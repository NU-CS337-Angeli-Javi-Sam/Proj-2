from nltk.stem.snowball import SnowballStemmer
from data_structures.ontologies.CookingActions import CookingActionsOntology
from data_structures.ontologies.Ingredients import IngredientOntology
from data_structures.ontologies.Measurements import MeasurementsOntology
from data_structures.ontologies.CookingTools import CookingToolsOntology
from nltk.stem.snowball import SnowballStemmer
import nltk
from nltk import word_tokenize, pos_tag
import re
import unicodedata

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

stemmer = SnowballStemmer("english")

# Create Ontology objects
cooking_actions = CookingActionsOntology()
ingredients = IngredientOntology()
measurements = MeasurementsOntology()
tools = CookingToolsOntology()

class Ingredient:

    #Representation of ingredient in recipe
    def __init__(self, ingredient_sent):
        # Name logic
        self.__original_text = ingredient_sent
        self.__full_name = self.__set_full_name(ingredient_sent)
        self.__simplified_name = self.__set_simplified_name()

        # Amount logic
        self.__quantity = self.__set_quantity(ingredient_sent)

        # Qualities
        self.__qualities = self.__set_qualities(ingredient_sent)

    def __get_word_stem(self, word):
        return stemmer.stem(re.search(r'[A-Za-z]*', word).group(0))

    def __set_full_name(self, ingredient_sent):
        long_name_str = ""
        for measurement in measurements.categories.keys():
            name_regex = f'(?<=({measurement} ))[A-Za-z\s-]*'
            match = re.search(name_regex, ingredient_sent)

            if match:
                long_name_str = match.group()
                break

        if not match:
            match = re.search(r'[A-Za-z\s]+', ingredient_sent)
            long_name_str = match.group().strip()

        return long_name_str

    def __set_simplified_name(self):
        simplified_name_str = ""
        for ingredient_list in ingredients.categories.values():
            for ingredient in ingredient_list:
                if ingredient in self.get_full_name():
                    simplified_name_str = ingredient
                    break

        if not simplified_name_str:
            simplified_name_str = self.get_full_name()

        return simplified_name_str

    def __set_qualities(self, ingredient_sent):
        qualities_list = []
        normalized_sent = unicodedata.normalize('NFKC', ingredient_sent)

        # Get qualities following a comma
        match = re.search(r'(?<=, )[A-Za-z\s]*', normalized_sent)
        if match:
            qualities_list.append(match.group())

        # Get adjectives not included in simplified name
        sent_words = word_tokenize(normalized_sent)
        pos_tags = pos_tag(sent_words)

        for pos in pos_tags:
            if pos[1] == 'JJ' and pos[0] not in self.get_simplified_name(): # Is an adjective
                qualities_list.append(pos[0])

        return qualities_list

    def __set_quantity(self, ingredient_sent):
        normalized_sent = unicodedata.normalize('NFKC', ingredient_sent)
        quantity_str = ""

        for measurement in measurements.categories.keys():
            measurement_regex = f'\d+.*{measurement}'
            match = re.search(measurement_regex, normalized_sent)

            if match:
                quantity_str = match.group()
                break

        if not match:
            match = re.search(r'\d+', normalized_sent)
            # print(match1.group())
            if match:
                quantity_str = f"{match.group()} item(s)"

        return quantity_str

    def get_original_text(self):
        return self.__original_text

    def get_full_name(self):
        return self.__full_name

    def get_simplified_name(self):
        return self.__simplified_name

    def get_qualities(self):
        return self.__qualities

    def get_quantity(self):
        return self.__quantity

    def __str__(self):
        return f"Original text: {self.__original_text}\nFull name: {self.__full_name}\nSimplified Name: {self.__simplified_name}\nQualities: {self.__qualities}\nQuantity: {self.__quantity}\n\n"
