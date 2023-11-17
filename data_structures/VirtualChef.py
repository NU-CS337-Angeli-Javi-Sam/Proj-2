from typing import Union

from data_structures.Recipe import Recipe
from data_structures.Instruction import Instruction


class VirtualChef:
    def __init__(self) -> None:
        self.__recipe: Recipe = Recipe()
        self.__curr_step: int = 0
        self.__curr_instruction: Instruction = None


    def handle_utterance(self, utterance: str) -> str:
        utterance = utterance.lower()
        response = "I don't understand"

        # Query control
        if utterance[0] == 'how' or utterance[0] == 'what':
            response = self.get_query(utterance)

        # Step control
        if 'tell me' in utterance or 'go' in utterance:
            if 'next' in utterance:
                response = self.get_next_instruction()
            elif 'back' in utterance:
                response = self.get_prev_instruction()
            elif 'repeat' in utterance:
                if 'at' in utterance:
                    # response = self.get_instruction_at()
                    # return response
                    print(utterance)
                response = self.get_curr_instruction()
            elif 'go to' in utterance:
                # response = self.get_instruction_at()
                print(utterance)

        # Meta control
        if utterance == "show me all ingredients":

            response = self.get_all_ingredients()

        #Transformation
        if 'substitute' in utterance or 'substitution' in utterance:
            pass

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
            self.set_curr_instruction()
        else:
            self.set_curr_step(self.get_curr_step() - 1)
            self.set_curr_instruction("This is the beginning of the recipe.")


        return self.get_curr_instruction()

    def get_query(self, query) -> str:
        #Youtube Query
        query = query.split(' ')

        #Current step queries
        if 'temperature' in query:
            #Handle null temperature
            temperature = self.get_recipe().get_instruction(self.get_curr_step()).get_temperature()
            if not temperature:
                self.set_curr_instruction('This is no temperature on this step')
            else:
                self.set_curr_instruction(temperature)

            return self.get_curr_instruction()
        elif 'how long' in query:
            #Handle null time
            time = self.get_recipe().get_instruction(self.get_curr_step()).get_time()
            if not time:
                self.set_curr_instruction('This is no time on this step')
            else:
                self.set_curr_instruction(time)

            return self.get_curr_instruction()

        # General how-to
        # if 'this' in query or 'that' in query:
        #     actions = self.get_recipe().get_instruction(self.get_curr_step()).get_cooking_actions()
        #     ingredients = self.get_recipe().get_instruction(self.get_curr_step()).get_ingredients()
        #
        #     curr_index = self.

        query = '+'.join(query)

        self.set_curr_instruction(f"https://www.youtube.com/results?search_query={query}")

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
