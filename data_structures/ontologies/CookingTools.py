class CookingToolsOntology:
    def __init__(self):
        """
        Initializes a CookingActionsOntology instance with predefined cooking action categories and actions.

        The categories map cooking actions to their respective categories, making it easy to categorize actions.
        The lexicon is a dictionary that maps specific cooking actions to their corresponding categories.

        Example:
        {
            "Heat": ["bake", "boil", ...],
            "Prepare": ["chop", "dice", ...],
            ...
        }
        """

        self.categories = {
            "Cutting Tools": ["knife", "scissors", "mandoline", "peeler", "grater", "zester", "shears", "cleaver", "paring knife", "bread knife"],
            "Cooking Vessels": ["pot", "pan", "skillet", "wok", "saucepan", "roasting pan", "casserole dish", "stockpot", "Dutch oven", "grill pan"],
            "Baking Tools": ["oven", "baking sheet", "rolling pin", "muffin tin", "cake pan", "cookie cutter", "pastry brush", "baking stone", "pie dish", "bread pan"],
            "Mixing Tools": ["spoon", "whisk", "spatula", "mixing bowl", "stand mixer", "hand mixer", "food processor", "blender", "measuring cups", "mixing spoon"],
            "Grilling Tools": ["grill", "tongs", "grill brush", "basting brush", "smoker box", "grill basket", "skewers", "heat-resistant gloves", "instant-read thermometer", "grill grates"],
            "Specialized Tools": ["sous-vide machine", "blowtorch", "microplane", "mortar and pestle", "pepper mill", "pasta maker", "thermometer", "food scale", "strainer", "mandoline slicer"],
        }

        self.lexicon = {}
        for category, tools in self.categories.items():
            for tool in tools:
                self.lexicon[tool] = category

    def get_category(self, tool):
        """
        Get the category for a given cooking action.

        Parameters:
        - action (str): The cooking action to retrieve the category for.

        Returns:
        - str: The category associated with the provided cooking action. If the action is not found, it returns "Unknown."
        """
        return self.lexicon.get(tool, "Unknown")
