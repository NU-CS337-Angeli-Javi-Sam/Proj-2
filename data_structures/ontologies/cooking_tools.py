class CookingToolsOntology:
    def __init__(self):
        self.categories = {
            "Cutting Tools": ["knife", "scissors", "mandoline", "peeler", "grater", "zester", "shears", "cleaver", "paring knife", "bread knife"],
            "Cooking Vessels": ["pot", "pan", "skillet", "wok", "saucepan", "roasting pan", "casserole dish", "stockpot", "Dutch oven", "grill pan"],
            "Baking Tools": ["oven", "baking sheet", "rolling pin", "muffin tin", "cake pan", "cookie cutter", "pastry brush", "baking stone", "pie dish", "bread pan"],
            "Mixing Tools": ["spoon", "whisk", "spatula", "mixing bowl", "stand mixer", "hand mixer", "food processor", "blender", "measuring cups", "mixing spoon"],
            "Grilling Tools": ["grill", "tongs", "grill brush", "basting brush", "smoker box", "grill basket", "skewers", "heat-resistant gloves", "instant-read thermometer", "grill grates"],
            "Specialized Tools": ["sous-vide machine", "blowtorch", "microplane", "mortar and pestle", "pepper mill", "pasta maker", "thermometer", "food scale", "strainer", "mandoline slicer"],
        }
        self.lexicon = {tool: category for category, tools in self.categories.items() for tool in tools}

    def get_category(self, tool):
        return self.lexicon.get(tool, "Unknown")
