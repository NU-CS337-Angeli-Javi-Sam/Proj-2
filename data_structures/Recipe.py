from typing import Dict, List
from data_structures.DoublyLinkedList import DoublyLinkedList
from data_structures.Ingredient import Ingredient
from data_structures.Instruction import Instruction

class Recipe:
    def __init__(self) -> None:
        self.__name = ""
        self.__ingredients = {}
        self.__instructions = DoublyLinkedList()
        self.__cook_time = {}
        self.__total_time = {}

    def __str__(self) -> str:
        output = f"Recipe Name: {self.get_name()}\n\n"
        output += f"Recipe Ingredients:\n\n"

        for ingredient in self.get_ingredients().keys():
            output += f"  - {ingredient}"

            output += "\n\n"

        output += str(self.get_instructions())

        return output

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def add_ingredient(self, name: str, ingredient: Ingredient) -> None:
        self.__ingredients[name] = ingredient

    def add_ingredients(self, ingredients: Dict["str", "Ingredient"]) -> None:
        for name, ingredient in ingredients.items():
            self.add_ingredient(name, ingredient)

    def get_ingredients(self) -> Dict["str", Ingredient]:
        return self.__ingredients

    def get_ingredient(self, ingredient_name: str):
        return self.get_ingredients()[ingredient_name]

    def add_instruction(self, instruction: Instruction) -> None:
        self.__instructions.append(instruction)

    def add_instructions(self, instructions: List["Instruction"]) -> None:
        for instruction in instructions:
            self.add_instruction(instruction)

    def get_instructions(self) -> DoublyLinkedList:
        return self.__instructions

    def get_instruction(self, index: int) -> Instruction:
        self.__instructions.get_data_at(index)

    def get_instruction_count(self) -> int:
        return self.__instructions.get_length()


    #
    #
    #
    # NEED TO UNDERSTAND THE FINAL OUTPUT FORMAT BEFORE CREATING THESE METHODS
    #
    #
    #

    # def add_total_time(self, quantity: float, metric: str) -> None:
    #     time_data = {
    #         "quantity": quantity,
    #         "metric": metric
    #     }
    #     self.__total_time = time_data

    # def get_total_time(self) -> Dict["str", Union["float", "str"]]:
    #         return self.__total_time

    # def get_total_time_quantity(self) -> float:
    #     return self.get_total_time()["quantity"]

    # def get_total_time_metric(self) -> str:
    #     return self.get_total_time()["metric"]

    # def add_cook_time(self, quantity: float, metric: str) -> None:
    #     time_data = {
    #         "quantity": quantity,
    #         "metric": metric
    #     }
    #     self.__cook_time = time_data

    # def get_cook_time(self) -> Dict["str", Union["float", "str"]]:
    #     return self.__cook_time

    # def get_cook_time_quantity(self) -> float:
    #     return self.get_cook_time()["quantity"]

    # def get_cook_time_metric(self) -> str:
    #     return self.get_cook_time()["metric"]
