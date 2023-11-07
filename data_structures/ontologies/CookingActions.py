class CookingActionsOntology:
    def __init__(self):
        self.categories = {
            "Heat": ["bake", "boil", "broil", "simmer", "fry", "grill", "roast", "saute", "steam", "sear", "melt", "heat", "chill", "reheat"],
            "Prepare": ["chop", "dice", "mince", "slice", "grate", "peel", "trim", "shred", "mash", "cut", "carve", "quarter", "divide", "strip", "crumple", "cut", "decorate", "fold", "form", "moisten", "puree", "season", "set", "sprinkle", "strew", "taste", "thin", "tie", "top", "trim", "turn", "twist", "wilt", "wind", "wrap"],
            "Mix": ["stir", "whisk", "blend", "fold", "knead", "mix", "combine"],
            "Bake": ["bake", "roast", "broil", "roll"],
            "Simmer": ["simmer", "boil", "stew"],
            "Fry": ["fry", "deep-fry", "pan-fry"],
            "Grill": ["grill", "barbecue"],
            "Roast": ["roast", "bake", "roll"],
            "Saute": ["saute", "pan-fry", "sear"],
            "Steam": ["steam", "poach"],
            "Cut": ["cut", "slice", "chop", "dice", "mince", "shred", "carve", "quarter", "divide", "strip"],
            "Measure": ["measure", "weigh"],
            "Serve": ["serve", "plate", "garnish", "taste"],
            "General Kitchen Actions": ["press", "remove", "set", "drain", "use", "adjust", "cover", "store", "discard", "close", "open", "drop", "pack", "raise", "refresh", "ring", "salt", "scatter", "scrape", "scrub", "separate", "settle", "shave", "skim", "slide", "slip", "slit", "smear", "soak", "spoon", "spread", "stir", "strain", "stuff", "surround", "tilt", "tip", "toss"],
        }

        self.lexicon = {}
        for category, actions in self.categories.items():
            for action in actions:
                self.lexicon[action] = category

    def get_category(self, action):
        return self.lexicon.get(action, "Unknown")
