from typing import Union

from data_structures.Recipe import Recipe
from data_structures.Instruction import Instruction

import re


class VirtualChef:
    # Utterances keywords in regex
    contexts = {
        'navigation': [r'(go|take).*step.*', r'what is.*step.*', r'repeat', r'next', r'back'],
        'meta': [r'ingredients list', r'all.*ingredients', r'all.*tools', r'all.*utensils', r'all.*step',
                  r'name.*recipe', r'recipe.*name', r'ingredients', r'tools'],
        'transformation': [r'change', r'substitute', r'vegetarian', r'gluten.free', r'kosher', r'halal', r'indian',
                            r'italian', r'mexican'],
        'query': [r'what|how']
    }

    # Query for when we don't know how to answer the question
    YOUTUBE_URL = "https://www.youtube.com/results?search_query="
    GOOGLE_URL = "https://www.google.com/search?q="

    def __init__(self) -> None:
        self.__recipe: Recipe = Recipe()
        self.__curr_step: int = -1
        self.__curr_instruction: Instruction = None

    def handle_utterance(self, utterance: str) -> str:
        #Use regexes to filter the type of questions the user is asking
        utterance = utterance.lower()

        response = ''
        for context, regex_list in self.contexts.items():
            match = None
            for regex in regex_list:
                match = re.search(regex, utterance)

                if match != None:
                    break

            if match != None:
                if context == 'navigation':
                    response = self.__handle_navigation_utterance(match.string)
                elif context == 'meta':
                    response = self.__handle_meta_utterance(match.string)
                elif context == 'transformation':
                    response = self.__handle_transformation_utterance(match.string)
                elif context == 'query':
                    response = self.__handle_query_utterance(match.string, utterance)

                break

        if response == '':
            return "I don't understand, idiot sandwich"

        return response

    def __handle_navigation_utterance(self, match):
        response = ''

        #Direction
        if 'next' in match:
            response = self.get_next_instruction().get_instruction()
        elif 'back' in match or 'previous' in match or 'prev' in match:
            response = self.get_prev_instruction().get_instruction()
        elif 'go' in match or 'take' in match:
            if 'next' in match:
                response = self.get_next_instruction().get_instruction()
            elif 'back' in match or 'previous' in match or 'prev' in match:
                response = self.get_prev_instruction().get_instruction()
        elif 'repeat' in match:
            response = self.get_curr_instruction().get_instruction()
        #Step index
        elif 'what is':
            number_regex = r'[0-9]+'
            step_number = int(re.search(number_regex, match).group())
            if step_number:
                self.set_curr_step(step_number - 1)
                response = self.get_instruction_at(step_number)

        return response

    def __handle_meta_utterance(self, match):
        response = ''

        #All Ingredients
        if 'ingredients' in match:
            response += self.get_all_ingredients()

        #All Tools
        elif 'tools' in match or 'utensils' in match:
            response += self.get_all_tools()

        #All Steps
        elif 'step' in match:
            instructions_linked_list = self.get_recipe().get_instructions()

            for index in range(0, instructions_linked_list.get_length()):
                response += instructions_linked_list.get_node_at(index).get_instruction() + ' \n'
        #Recipe Name
        elif 'name' in match and 'recipe' in match:
            response += self.get_recipe().get_name()

        return response

    def __handle_transformation_utterance(self, match):
        pass

    def __handle_query_utterance(self, match, query):
        response = ''

        #Parameters
        if 'how long' in match:
            time = self.get_curr_instruction().get_time()

            response += "Timing is crucial in the kitchen, my friend. For this step, it's all about precision. Now, let me tell you, there's no one-size-fits-all answer; it depends on the dish and the technique. Keep a watchful eye, trust your instincts, and don't rush the process.\n\n"
            if time:
                response += f"Do this step for about {time}."
            else:
                response = 'Fortunately, there is no time requirement at this step.'

        elif 'what temp' in match or 'how hot' in match or 'how cold' in match or 'what temperature' in match:
            temperature = self.get_curr_instruction().get_temp()

            response += "Ah, temperature, the secret conductor of the culinary orchestra. For this step, precision is key. Now, the optimal temperature can vary depending on what we're cooking. If you're following a recipe, it should have a guideline.\n\n"

            if temperature:
                response += f"Perform this step at about {temperature}"
            else:
                response += 'Fortunately, there is no temperature requirement at this step.'

        elif 'how much' in match or 'how many' in match:
            temp_query = query.replace(" of ", " ")
            # Get the ingredient name only
            ingredient_regex = r'(?<=(how many|how much) )[A-Za-z]*'
            ingredient_match = re.search(ingredient_regex, temp_query)

            # Get all the ingredients in the current instruction
            ingredients_items = self.get_curr_instruction().get_ingredients()

            # Fetch the quantity
            if 'how much' in match or 'how many' in match:
                response += "Ah, the dance of measurements—the heartbeat of precision in the kitchen. When it comes to 'how much,' it's a delicate balance. The right amount can make or break a dish. If you're following a recipe, it should lay out the quantities for you.\n\n"

                quantity = -1
                for ingredient_obj in ingredients_items.values():
                    if ingredient_match.group(0) in ingredient_obj.get_full_name():
                        quantity = ingredient_obj.get_quantity()
                        response += f"This step requires {quantity} {ingredient_obj.get_full_name()}."

                # Response if no quantity found
                if quantity == -1:
                    response += f"I'm not sure how much {ingredient_match.group(0)} is required."

        if response != '':
            return response

        response = "Hold on a moment, let me grab you a reference from the web to give you the most accurate and detailed information. The kitchen is like a treasure trove of knowledge, and we want to make sure we're slicing through it with precision. Just a brief moment, and we'll have your answer ready. Thanks for your patience!\n\n"
        if "what is" in match or "what are" in match:
            url = self.GOOGLE_URL + "+".join(query.split(" "))
            response += f"Here is a reference for your question: {url}"

        #Simple "What is" and Specific "How to"
        elif 'how to' in match or 'how do' in match or 'how should' in match:
            #Vague "How to"
            if "that" in match or "this" in match:
                query = 'how to ' + self.get_curr_instruction().get_instruction().lower()

            url = self.YOUTUBE_URL + "+".join(query.split(" "))
            response += f"Here is a reference for your question: {url}"

        return response

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
            self.set_curr_instruction(self.get_curr_step())
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
        ingredients = 'Ingredients:\n\n'

        for ingredient in self.get_recipe().get_ingredients().values():
            ingredients += f'- {ingredient.get_original_text()}\n\n'

        return ingredients

    def get_all_tools(self) -> str:
        tools = '\nTools:'

        for tool in self.get_recipe().get_tools():
            tools += f'\n\n - {tool}'

<<<<<<< Updated upstream
        return tools
=======
        return tools
>>>>>>> Stashed changes
