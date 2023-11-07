
class Instruction(Node):
    def __init__(self):
        # Give each Instruction __next and __prev variables
        super().__init__()

        self.__utensils = None
        self.__ingredients = None
        self.__cooking_actions = None
        self.__temperature = None
        self.__time = None
        

