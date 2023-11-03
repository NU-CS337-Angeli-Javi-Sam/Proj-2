class IngredientOntology:
    def __init__(self):
        self.categories = {
            "Fruits": ["apple", "banana", "orange", "strawberry", "kiwi", "mango", "grape", "lemon", "blueberry", "watermelon"],
            "Vegetables": ["carrot", "broccoli", "spinach", "zucchini", "potato", "onion", "tomato", "bell pepper", "cucumber", "mushroom"],
            "Proteins": ["chicken", "beef", "salmon", "tofu", "shrimp", "pork", "lamb", "turkey", "egg", "bacon"],
            "Grains": ["rice", "pasta", "quinoa", "oats", "barley", "couscous", "bulgur", "bread", "corn", "wheat"],
            "Dairy": ["milk", "cheese", "yogurt", "butter", "cream", "eggnog", "sour cream", "cream cheese", "cottage cheese", "whipped cream"],
            "Herbs and Spices": ["basil", "thyme", "rosemary", "cumin", "coriander", "cinnamon", "paprika", "ginger", "nutmeg", "oregano"],
            "Oils and Condiments": ["olive oil", "soy sauce", "vinegar", "ketchup", "mayonnaise", "mustard", "hot sauce", "honey", "maple syrup", "sesame oil"],
            "Canned and Packaged": ["canned tomatoes", "canned beans", "chicken broth", "coconut milk", "pasta sauce", "cereal", "canned tuna", "peanut butter", "instant noodles", "canned vegetables"],
            "Nuts and Seeds": ["almonds", "walnuts", "sunflower seeds", "flaxseeds", "cashews", "peanuts", "sesame seeds", "pumpkin seeds", "chia seeds", "pecans"],
            "Sweets and Desserts": ["sugar", "chocolate", "vanilla extract", "honey", "caramel", "marshmallows", "cookies", "cake", "ice cream", "candies"],
        }
        self.lexicon = {ingredient: category for category, ingredients in self.categories.items() for ingredient in ingredients}

    def get_category(self, ingredient):
        return self.lexicon.get(ingredient, "Unknown")
