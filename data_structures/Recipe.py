from typing import Dict, List
from data_structures.DoublyLinkedList import DoublyLinkedList
from data_structures.Ingredient import Ingredient
from data_structures.Instruction import Instruction

class Recipe:
    def __init__(self) -> None:
        """
        Initializes a Recipe instance with properties for name, ingredients, and instructions.

        The ingredients are stored as a dictionary, and the instructions are stored in a doubly linked list.
        """
        self.__name = ""
        self.__ingredients = {}
        self.__instructions = DoublyLinkedList()
        # self.__cook_time = {}
        # self.__total_time = {}

    def __str__(self) -> str:
        """
        Returns a string representation of the recipe, including its name, ingredients, and instructions.

        Returns:
        - str: A string representation of the recipe.
        """
        output = f"Recipe Name: {self.get_name()}\n\n"
        output += f"Recipe Ingredients:\n\n"

        for ingredient in self.get_ingredients().keys():
            output += f"  - {ingredient}"

            output += "\n\n"

        output += str(self.get_instructions())

        return output

    def set_name(self, name: str) -> None:
        """
        Set the name of the recipe.

        Parameters:
        - name (str): The name of the recipe.
        """
        self.__name = name

    def get_name(self) -> str:
        """
        Get the name of the recipe.

        Returns:
        - str: The name of the recipe.
        """
        return self.__name

    def add_ingredient(self, name: str, ingredient: Ingredient) -> None:
        """
        Add an ingredient to the recipe.

        Parameters:
        - name (str): The name of the ingredient.
        - ingredient (Ingredient): An instance of the Ingredient class representing the ingredient.
        """
        self.__ingredients[name] = ingredient

    def add_ingredients(self, ingredients: Dict["str", "Ingredient"]) -> None:
        """
        Add multiple ingredients to the recipe.

        Parameters:
        - ingredients (Dict[str, Ingredient]): A dictionary of ingredient names and Ingredient instances.
        """
        for name, ingredient in ingredients.items():
            self.add_ingredient(name, ingredient)

    def get_ingredients(self) -> Dict["str", Ingredient]:
        """
        Get the ingredients of the recipe.

        Returns:
        - Dict[str, Ingredient]: A dictionary of ingredient names and their corresponding Ingredient instances.
        """
        return self.__ingredients

    def get_ingredient(self, ingredient_name: str):
        """
        Get a specific ingredient from the recipe.

        Parameters:
        - ingredient_name (str): The name of the ingredient to retrieve.

        Returns:
        - Ingredient: An instance of the Ingredient class representing the specified ingredient.
        """
        return self.get_ingredients()[ingredient_name]

    def add_instruction(self, instruction: Instruction) -> None:
        """
        Add an instruction to the recipe.

        Parameters:
        - instruction (Instruction): An instance of the Instruction class representing the instruction.
        """
        self.__instructions.append(instruction)

    def add_instructions(self, instructions: List["Instruction"]) -> None:
        """
        Add multiple instructions to the recipe.

        Parameters:
        - instructions (List[Instruction]): A list of Instruction instances.
        """
        for instruction in instructions:
            self.add_instruction(instruction)

    def get_instructions(self) -> DoublyLinkedList:
        """
        Get the instructions of the recipe.

        Returns:
        - DoublyLinkedList: A doubly linked list containing the instructions of the recipe.
        """
        return self.__instructions

    def get_instruction(self, index: int) -> Instruction:
        """
        Get a specific instruction from the recipe by its index.

        Parameters:
        - index (int): The index of the instruction to retrieve.

        Returns:
        - Instruction: An instance of the Instruction class representing the specified instruction.
        """
        self.__instructions.get_data_at(index)

    def get_instruction_count(self) -> int:
        """
        Get the total number of instructions in the recipe.

        Returns:
        - int: The count of instructions in the recipe.
        """
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
