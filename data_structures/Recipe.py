from data_structures.DoublyLinkedList import DoublyLinkedList

class Recipe:
    def __init__(self) -> None:
        self.__name = ""
        self.__ingredients = {}
        self.__instructions = DoublyLinkedList()

    def __str__(self) -> str:
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"

    def get_name(self) -> str:
        return self.__name

    def get_ingredients(self) -> dict:
        return self.__ingredients

    def get_instruction(self) -> DoublyLinkedList:
        return self.__instructions

    def set_name(self, name: str) -> None:
        self.__name = name

    def add_ingredient(self, name: str, quantity: float, metric: str) -> None:
        ingredient_data = {
            "quantity": quantity,
            "metric": metric
        }
        self.__ingredients[name] = ingredient_data

    def get_ingredient_info(self, ingredient: str) -> dict:
        return self.get_ingredients()[ingredient]

    def get_ingredient_quantity(self, ingredient: str) -> float:
        return self.get_ingredient_info(ingredient)["quantity"]

    def get_ingredient_metric(self, ingredient: str) -> str:
        return self.get_ingredient_info(ingredient)["metric"]

    def add_instruction(self, instruction: str) -> None:
        self.__instructions.append(instruction)
