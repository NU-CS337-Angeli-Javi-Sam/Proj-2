class MeasurementsOntology:
    def __init__(self):
        self.categories = {
            "hour": ["hr", "hr.", "hour", "hours"],
            "minute": ["min.", "min", "minutes", "minute"],
            "inch": ["\"\"", "in.", "inch", "in", "inches"],
            "tablespoon": ["tbsp.", "Tbsp.", "Tb.", "T."],
            "teaspoon": ["tsp.", "ts."],
            "ounce": ["oz.", "ozs."],
            "pound": ["lb.", "lbs."],
            "cup": ["cup", "cups"],
            "quart": ["quart", "quarts"],
            "gallon": ["gallon", "gallons"],
            "milliliter": ["ml.", "mls."],
            "liter": ["liter", "liters"],
            "pinch": ["pinch", "pinches"],
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
            "a touch of": ["a touch of"],
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
        return self.lexicon.get(measurement, "Unknown")
