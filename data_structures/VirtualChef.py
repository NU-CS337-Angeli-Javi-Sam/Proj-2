from data_structures.Recipe import Recipe


class VirtualChef:
    def __init__(self) -> None:
        self.__recipe = Recipe()
        self.__curr_step = 0
        self.__curr_instruction = "Please enter the recipe you'd like my help with."

    def get_recipe(self) -> Recipe:
        return self.__recipe

    def get_curr_step(self) -> int:
        return self.__curr_step

    def get_curr_instruction(self) -> str:
        return self.__curr_instruction

    def set_recipe(self, recipe: Recipe) -> None:
        self.__recipe = recipe

    def set_curr_step(self, step: int) -> None:
        self.__curr_step = step

    def set_curr_instruction(self, step: int) -> None:
        curr_instruction = self.get_recipe().get_instruction(step)
        self.__curr_instruction = curr_instruction

    def get_next_instruction(self) -> str:
        if self.get_curr_step() != self.get_recipe().get_instruction_count():
            self.set_curr_step(self.get_curr_step() + 1)
            self.set_curr_instruction(self.get_curr_step())
        else:
            self.set_curr_step(self.get_curr_step() + 1)
            self.set_curr_instruction("You've reached the end of the recipe.")

        return self.get_curr_instruction()

    def get_prev_instruction(self) -> str:
        if self.get_curr_step() != 0:
            self.set_curr_step(self.get_curr_step() - 1)
            self.set_curr_instruction(self.get_curr_step())
        else:
            self.set_curr_instruction("This is the first instruction of the recipe.")

        return self.get_curr_instruction()
