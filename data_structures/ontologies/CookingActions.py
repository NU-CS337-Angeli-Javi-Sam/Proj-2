class CookingActionsOntology:
    def __init__(self):
        self.categories = {
            "Heat": ["bake", "boil", "broil", "simmer", "fry", "grill", "roast", "saute", "steam", "sear", "melt", "heat", "chill"],
            "Prepare": ["chop", "dice", "mince", "slice", "grate", "peel", "trim", "shred", "mash"],
            "Mix": ["stir", "whisk", "blend", "fold", "knead"],
            "Bake": ["bake", "roast", "broil"],
            "Simmer": ["simmer", "boil", "stew"],
            "Fry": ["fry", "deep-fry", "pan-fry"],
            "Grill": ["grill", "barbecue"],
            "Roast": ["roast", "bake"],
            "Saute": ["saute", "pan-fry", "sear"],
            "Steam": ["steam", "poach"],
            "Cut": ["chop", "dice", "mince", "slice", "grate"],
            "Mix": ["stir", "whisk", "blend", "fold", "knead"],
            "Measure": ["measure", "weigh"],
            "Serve": ["serve", "plate", "garnish", "taste", "serve", "serve"],
            "Prepare Ingredients": ["prep", "clean", "peel", "trim", "grate"],
            "General Kitchen Actions": ["press", "remove", "replace", "use", "adjust", "cover", "store", "reheat", "discard"],
        }

        self.lexicon = {}
        for category, actions in self.categories.items():
            for action in actions:
                self.lexicon[action] = category

    def get_category(self, action):
        return self.lexicon.get(action, "Unknown")
