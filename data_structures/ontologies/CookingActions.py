class CookingActionsOntology:
    def __init__(self):
        self.categories = {
            "Heat": ["bake", "boil", "broil", "simmer", "fry", "grill", "roast", "saute", "steam"],
            "Prepare": ["chop", "dice", "mince", "slice", "grate", "peel", "trim", "shred"],
            "Mix": ["stir", "whisk", "blend", "fold", "knead"],
            "Bake": ["bake", "roast", "broil"],
            "Simmer": ["simmer", "boil", "stew"],
            "Fry": ["fry", "deep-fry", "pan-fry"],
            "Grill": ["grill", "barbecue"],
            "Roast": ["roast", "bake"],
            "Saute": ["saute", "pan-fry"],
            "Steam": ["steam", "poach"],
            "Cut": ["chop", "dice", "mince", "slice", "grate"],
            "Mix": ["stir", "whisk", "blend", "fold", "knead"],
            "Measure": ["measure", "weigh"],
            "Serve": ["serve", "plate", "garnish"],
            "Prepare Ingredients": ["prep", "clean", "peel", "trim", "grate"],
        }
        self.lexicon = { action: category for action, category in self.categories.items()}

    def get_category(self, ingredient):
        return self.lexicon.get(ingredient, "Unknown")
