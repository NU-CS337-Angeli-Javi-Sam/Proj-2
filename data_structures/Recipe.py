from typing import Dict, Union
from data_structures.DoublyLinkedList import DoublyLinkedList
from data_structures.Ingredient import Ingredient

class Recipe:
    def __init__(self) -> None:
        self.__name = ""
        self.__ingredients = {}
        self.__instructions = DoublyLinkedList()
        self.__cook_time = {}
        self.__total_time = {}
        self.__instruction_count = 0

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def add_ingredient(self, name: str, ingredient: Ingredient) -> None:
        self.__ingredients[name] = ingredient

    def get_ingredients(self) -> Dict["str", Ingredient]:
        return self.__ingredients

    def get_ingredient(self, ingredient_name: str):
        return self.get_ingredients()[ingredient_name]

    def add_instruction(self, instruction: str) -> None:
        self.__instructions.append(instruction)
        self.__instruction_count = self.get_instruction_count() + 1

    def get_instructions(self) -> DoublyLinkedList:
        return self.__instructions

    def get_instruction(self, index: int) -> str:
        self.__instructions.get_data_at(index)

    def get_instruction_count(self) -> int:
        return self.__instruction_count

    def add_total_time(self, quantity: float, metric: str) -> None:
        time_data = {
            "quantity": quantity,
            "metric": metric
        }
        self.__total_time = time_data

    def get_total_time(self) -> Dict["str", Union["float", "str"]]:
            return self.__total_time

    def get_total_time_quantity(self) -> float:
        return self.get_total_time()["quantity"]

    def get_total_time_metric(self) -> str:
        return self.get_total_time()["metric"]

    def add_cook_time(self, quantity: float, metric: str) -> None:
        time_data = {
            "quantity": quantity,
            "metric": metric
        }
        self.__cook_time = time_data

    def get_cook_time(self) -> Dict["str", Union["float", "str"]]:
        return self.__cook_time

    def get_cook_time_quantity(self) -> float:
        return self.get_cook_time()["quantity"]

    def get_cook_time_metric(self) -> str:
        return self.get_cook_time()["metric"]
