class MeasurementsOntology:
    def __init__(self):
        self.categories = {
            "tablespoon": ["tbsp.", "Tbsp.", "Tb.", "T."],
            "teaspoon": ["tsp.", "ts."],
            "ounce": ["oz.", "ozs."],
            "pound": ["lb.", "lbs."],
            "minute": ["min."],
            "inch": ["\"\""] 
        }

        self.lexicon = {}
        for category, measurement in self.categories.items():
            for variant in measurement:
                self.lexicon[variant] = category

    def get_category(self, measurement):
        return self.lexicon.get(measurement, "Unknown")
