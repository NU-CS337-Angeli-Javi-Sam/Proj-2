from typing import Dict, Optional, Union
from data_structures.DoublyLinkedList import DoublyLinkedList

class Recipe:
    def __init__(self) -> None:
        self.__name = ""
        self.__ingredients = {}
        self.__instructions = DoublyLinkedList()
        self.__cook_time = {}
        self.__total_time = {}
        self.__instruction_count = 0

    def get_name(self) -> str:
        return self.__name

    def get_ingredients(self) -> Dict["str", Dict["str", Union["float", "str"]]]:
        return self.__ingredients

    def get_instructions(self) -> DoublyLinkedList:
        return self.__instructions

    def get_instruction_count(self) -> int:
        return self.__instruction_count

    def set_name(self, name: str) -> None:
        self.__name = name

    def add_ingredient(self, name: str, quantity: float, metric: Optional["str"]=None) -> None:
        ingredient_data = {
            "quantity": quantity,
            "metric": metric
        }
        self.__ingredients[name] = ingredient_data

    def get_ingredient_info(self, ingredient: str) -> Dict["str", Union["float", "str"]]:
        return self.get_ingredients()[ingredient]

    def get_ingredient_quantity(self, ingredient: str) -> float:
        return self.get_ingredient_info(ingredient)["quantity"]

    def get_ingredient_metric(self, ingredient: str) -> str:
        return self.get_ingredient_info(ingredient)["metric"]

    def add_instruction(self, instruction: str) -> None:
        self.__instructions.append(instruction)
        self.__instruction_count = self.get_instruction_count() + 1

    def get_instruction(self, index: int) -> str:
        self.__instructions.get_data_at(index)

    def add_total_time(self, quantity: float, metric: str) -> None:
        time_data = {
            "quantity": quantity,
            "metric": metric
        }
        self.__total_time = time_data

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

    def get_total_time(self) -> Dict["str", Union["float", "str"]]:
        return self.__total_time

    def get_total_time_quantity(self) -> float:
        return self.get_total_time()["quantity"]

    def get_total_time_metric(self) -> str:
        return self.get_total_time()["metric"]
