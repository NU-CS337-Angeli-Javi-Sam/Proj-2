from typing import Union

from data_structures.Recipe import Recipe
from data_structures.Instruction import Instruction

import re


class VirtualChef:
    # Utterances keywords in regex
    contexts = {
        'navigation': [r'(go|take).*step.', r'what is.*step .', r'repeat.*step .', 'next.'],
        'meta': [r'ingredients list', r'all.*ingredients', r'all.*tools', r'all.*utensils', r'all.*step',
                  r'name.*recipe', r'recipe.*name'],
        'transformation': [r'change', r'substitute', r'vegetarian', r'gluten.free', r'kosher', r'halal', r'indian',
                            r'italian', r'mexican'],
        'query': [r'what are', r'what is', r'how long', r'how much', r'how to', r'how do', r'how should']
    }

    # Query for when we don't know how to answer the question
    YOUTUBE_URL = "https://www.youtube.com/results?search_query="

    def __init__(self) -> None:
        self.__recipe: Recipe = Recipe()
        self.__curr_step: int = 0
        self.__curr_instruction: Instruction = None

    def handle_utterance(self, utterance: str) -> str:
        #Use regexes to filter the type of questions the user is asking
        utterance = utterance.lower()

        for context, regex_list in self.contexts.items():
            for regex in regex_list:
                match = re.search(regex, utterance)

                if match:
                    response = ''

                    if context == 'navigation':
                        response = self.__handle_navigation_utterance(match.group(0))
                    elif context == 'meta':
                        response = self.__handle_meta_utterance(match.group(0))
                    elif context == 'transformation':
                        response = self.__handle_transformation_utterance(match.group(0))
                    elif context == 'query':
                        response = self.__handle_query_utterance(match.group(0), utterance)

                    return response

        return "I don't understand, idiot sandwich"

    def __handle_navigation_utterance(self, match):
        response = ''

        #Direction
        if 'go' in match or 'take' in match:
            if 'next' in match:
                response = self.get_next_instruction()
            elif 'back' in match or 'previous' in match or 'prev' in match:
                response = self.get_prev_instruction()
        elif 'repeat' in match:
            response = self.get_curr_instruction()
        #Step index
        elif 'what is':
            number_regex = r'[0-9]+'
            step_number = re.search(number_regex, match.group(0))
            if step_number:
                self.set_curr_step(int(step_number))
                response = self.get_instruction_at(int(step_number))

        return response

    def __handle_meta_utterance(self, match):
        response = ''

        #All Ingredients
        if 'ingredients' in match:
            for ingredient in self.get_recipe().get_ingredients().values():
                response += f'\n\n - {ingredient.get_original_text()}'
        #All Tools
        elif 'tools' in match or 'utensils' in match:
            instructions_linked_list = self.get_recipe().get_instructions()

            for index in range(0, instructions_linked_list.get_length()):
                response += instructions_linked_list.get_node_at(index).get_tools() + ' \n'
        #All Steps
        elif 'step' in match:
            instructions_linked_list = self.get_recipe().get_instructions()

            for index in range(0, instructions_linked_list.get_length()):
                response += instructions_linked_list.get_node_at(index).get_instruction() + ' \n'
        #Recipe Name
        elif 'name' in match and 'recipe' in match:
            response =  self.get_recipe().get_name()

        return response

    def __handle_transformation_utterance(self, match):
        pass

    def __handle_query_utterance(self, match, query):
        response = ''

        #Parameters
        if 'how long' in match:
            time = self.get_recipe().get_instruction(self.get_curr_step()) .get_time()
            if time:
                response = time
            else:
                response = 'No time at this step'

        elif 'how much' in match:
            #Quality for the ingredient they are talking about
            pass

        elif 'how should' in match:
            #Modifier for the ingredient they are talking about
            pass

        #Simple "What is" and Specific "How to"
        if 'what is' in match or 'what are' in match or 'how to' in match or 'how do' in match or 'how should' in match:
            #Vague "How to"
            if 'how' in match:
                if 'that' in match or 'this' in match:
                    query = 'how' + self.get_curr_instruction()

            response = self.YOUTUBE_URL + query.join('+')

    def get_recipe(self) -> Recipe:
        return self.__recipe

    def get_curr_step(self) -> int:
        return self.__curr_step

    def get_curr_instruction(self) -> Instruction:
        return self.__curr_instruction

    def set_recipe(self, recipe: Recipe) -> None:
        self.__recipe = recipe

    def set_curr_step(self, step: int) -> None:
        self.__curr_step = step

    def set_curr_instruction(self, step: Union[str, int]) -> None:
        curr_instruction = None

        if type(step) == int:
            curr_instruction = self.get_recipe().get_instruction(step)
        elif type(step) == str:
            curr_instruction = step

        self.__curr_instruction = curr_instruction

    def get_next_instruction(self) -> Instruction:

        if self.get_curr_step() != self.get_recipe().get_instruction_count():
            self.set_curr_step(self.get_curr_step() + 1)
            self.set_curr_instruction(self.get_curr_step())
        else:
            self.set_curr_step(self.get_curr_step() + 1)
            self.set_curr_instruction("You've reached the end of the recipe.")

        return self.get_curr_instruction()

    def get_prev_instruction(self) -> Instruction:
        if self.get_curr_step() != 0:
            self.set_curr_step(self.get_curr_step() - 1)
            self.set_curr_instruction()
        else:
            self.set_curr_step(self.get_curr_step() - 1)
            self.set_curr_instruction("This is the beginning of the recipe.")


        return self.get_curr_instruction()

    def get_instruction_at(self, index: int) -> Instruction:
        instruction = None

        try:
            instruction: Instruction = self.get_recipe().get_instructions().get_node_at(index)
        except Exception as e:
            self.set_curr_instruction("No step at that index, please input a valid index")
            return self.get_curr_instruction()

        self.set_curr_step(index)
        self.set_curr_instruction(instruction.get_instruction())

        return self.get_curr_instruction()

    def get_all_ingredients(self) -> str:
        ingredients = '\nIngredients:'

        for ingredient in self.get_recipe().get_ingredients().values():
            ingredients += f'\n\n - {ingredient.get_original_text()}'

        return ingredients
