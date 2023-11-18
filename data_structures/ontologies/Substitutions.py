class SubstitutionOntologies:
    def __init__(self):
        self.categories = {
            'vegetarian': {
                'Proteins': ['tofu', 'lentils', 'soybeans', 'chickpeas', 'tempeh']
            },
            'halal/kosher': {
            },
            'mexican': {
            },
            'metric': {
            }
        }

    """
        "Fruits"
        "Vegetables"
        "Proteins"
        "Grains"
        "Dairy"
        "Herbs and Spices"
        "Oils and Condiments"
        "Canned and Packaged"
        "Nuts and Seeds"
        "Sweets and Desserts"
    """


    def getCategory(self, variation, recipe):
        ingredients = recipe.get_ingredients()
        steps = recipe.get_instructions()


        newIngredients = {}

        for ingredient in ingredients:
            if variation == 'vegetarian':
                pass
            elif variation == 'halal' or variation == 'kosher':
                #If salt, change to kosher salt
                pass
            elif variation == 'mexican':
                pass
            elif variation == 'healthy':
                pass
                #change proteins, dairy, and oils/condiments to low-fat
                #change grains to low-carb
                #low sugar for sweets and desserts

        pass

    def getMetric(self):
        pass
