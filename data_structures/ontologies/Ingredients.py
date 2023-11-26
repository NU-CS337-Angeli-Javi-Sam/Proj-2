class IngredientOntology:
    def __init__(self):
        """
        Initializes an IngredientOntology instance with predefined ingredient categories and ingredients.

        The categories map ingredients to their respective categories, making it easy to categorize ingredients.
        The lexicon is a dictionary that maps specific ingredients to their corresponding categories.

        Example:
        {
            "Fruits": ["apple", "banana", ...],
            "Vegetables": ["carrot", "broccoli", ...],
            ...
        }
        """
        self.categories = {
            "Canned and Packaged": ["canned tomato", "canned bean", "chicken broth", "coconut milk", "pasta sauce", "cereal", "canned tuna", "peanut butter", "instant noodle", "canned vegetable", "milk powder"],
            "Fruits": ["apple", "banana", "orange peel", "orange", "strawberry", "strawberries", "kiwi", "mango", "grape", "lemon", "blueberry", "blueberries", "watermelon", "cherry", "cherries"],
            "Vegetables": ["carrot", "olive", "broccoli", "spinach", "zucchini", "potato", "red onion", "yellow onion", "onion", "tomato", "bell pepper", "cucumber", "mushroom", "garlic powder", "garlic"],
            "Proteins": ["beans", "chicken", "beef", "brisket", "salmon", "tuna", "tilapia", "shellfish", "tofu", "shrimp", "pork", "lamb", "turkey", "egg", "bacon", "cod", "mackerel", "crab", "lobster", "sardine", "steak", "flank steak", "chunk roast"],
            "Grains": ["flour", "semolina", "rice", "pasta", "quinoa", "oats", "barley", "couscous", "bulgur", "bread", "corn", "wheat", "panko"],
            "Dairy": ["cream cheese", "sour cream", "cottage cheese", "whipped cream", "cheddar", "milk", "cheese", "yogurt", "butter", "cream", "eggnog", "paneer"],
            "Herbs and Spices": ["basil", "thyme", "rosemary", "cumin", "cilantro", "cardamom", "coriander", "cinnamon", "paprika", "ginger", "nutmeg", "oregano", "pepper", "salt", "parsley", "turmeric", "chile powder", "asafetida powder", "bay leaves"],
            "Cooking Mediums and Condiments": ["water", "broth", "olive oil", "vegetable oil", "soy sauce", "baking powder", "vinegar", "ketchup", "mayonnaise", "mustard", "hot sauce", "honey", "maple syrup", "sesame oil", "ghee"],
            "Liquor": ["wine", "white wine", "red wine", "bitter", "simple syrup", "syrup", "rye", "bourbon", "rum", "vodka", "whiskey"],
            "Nuts and Seeds": ["almond", "walnut", "sunflower seed", "flaxseed", "cashew", "peanut", "sesame seed", "pumpkin seed", "chia seed", "pecan", "pistachio"],
            "Sweets and Desserts": ["sugar", "chocolate", "vanilla extract", "honey", "caramel", "marshmallows", "cookies", "cake", "ice cream", "cand"],
        }

        self.lexicon = {}
        for category, ingredients in self.categories.items():
            for ingredient in ingredients:
                self.lexicon[ingredient] = category

    def get_category(self, ingredient):
        """
        Get the category for a given ingredient.

        Parameters:
        - ingredient (str): The ingredient to retrieve the category for.

        Returns:
        - str: The category associated with the provided ingredient. If the ingredient is not found, it returns "Unknown."
        """
        return self.lexicon.get(ingredient, "Unknown")
