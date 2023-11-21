class MeasurementsOntology:
    def __init__(self):
        """
        Initializes a MeasurementsOntology instance with predefined measurement categories and their variants.

        The categories map measurement variants (e.g., abbreviations, synonyms) to their respective measurement categories.
        The lexicon is a dictionary that maps specific measurement variants to their corresponding categories.

        Example:
        {
            "hour": ["hr", "hr.", "hour", "hours"],
            "minute": ["min.", "min", "minutes", "minute"],
            ...
        }
        """
        self.categories = {
            "hour": ["hr", "hr.", "hour", "hours"],
            "minute": ["min.", "min", "minutes", "minute"],
            "inch": ["\"\"", "in.", "inch", "inches"],
            "tablespoon": ["tbsp.", "Tbsp.", "Tb.", "T.", "tablespoon"],
            "teaspoon": ["tsp.", "ts.", "teaspoon"],
            "ounce": ["oz.", "ozs.", "ounce"],
            "pound": ["lb.", "lbs.","pound"],
            "cup": ["cup", "cups"],
            "quart": ["quart", "quarts"],
            "gallon": ["gallon", "gallons"],
            "milliliter": ["ml.", "mls."],
            "liter": ["liter", "liters"],
            "pinch": ["pinch", "pinches"],
            "piece": ["piece", "pieces"],
            "dash": ["dash", "dashes"],
            "sprig": ["sprig", "sprigs"],
            "slice": ["slice", "slices"],
            "can": ["can", "cans"],
            "package": ["package", "packages"],
            "bunch": ["bunch", "bunches"],
            "clove": ["clove", "cloves"],
            "packet": ["packet", "packets"],
            "bag": ["bag", "bags"],
            "box": ["box", "boxes"],
            "jar": ["jar", "jars"],
            "bottle": ["bottle", "bottles"],
            "cube": ["cube", "cubes"],
            "head": ["head", "heads"],
            "ear": ["ear", "ears"],
            "stalk": ["stalk", "stalks"],
            "taste": ["taste", "tastes"],
            "stick": ["stick", "sticks"],
            "scoop": ["scoop", "scoops"],
            "portion": ["portion", "portions"],
            "dollop": ["dollop", "dollops"],
            "slab": ["slab", "slabs"],
            "shred": ["shred", "shreds"],
            "fillet": ["fillet", "fillets"],
            "chunk": ["chunk", "chunks"],
            "segment": ["segment", "segments"],
            "sprinkle": ["sprinkle", "sprinkles"],
            "drizzle": ["drizzle", "drizzles"],
            "splash": ["splash", "splashes"],
            "shot": ["shot", "shots"],
            "a touch of": ["a touch"],
            "serving": ["serving", "servings"],
            "loaf": ["loaf", "loaves"],
            "sheet": ["sheet", "sheets"],
            "leaf": ["leaf", "leaves"],
        }

        self.lexicon = {}
        for category, measurement in self.categories.items():
            for variant in measurement:
                self.lexicon[variant] = category

    def get_category(self, measurement):
        """
        Get the category for a given measurement variant.

        Parameters:
        - measurement (str): The measurement variant (e.g., abbreviation, synonym) to retrieve the category for.

        Returns:
        - str: The category associated with the provided measurement variant. If the variant is not found, it returns "Unknown."
        """
        return self.lexicon.get(measurement, "Unknown")
