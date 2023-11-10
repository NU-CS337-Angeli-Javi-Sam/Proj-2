from typing import Dict, List


class RecipeRelationships:
    def __init__(self) -> None:
        """
        Initializes a RecipeRelationships mappings between ingredients and tools, and actions.
        """
        self.action_ingredient_map: Dict[
            "str", List["str"]
        ] = self.create_action_ingredient_map()
        self.action_tool_map: Dict["str", List["str"]] = self.create_action_tool_map()

    def create_action_ingredient_map(self) -> Dict["str", List["str"]]:
        """
        Create a dictionary that maps cooking actions to the list of ingredients typically used for each action.

        Returns:
        - Dict[str, List[str]]: A dictionary where keys are cooking actions and values are lists of associated ingredients.
        """
        action_ingredient_map: Dict["str", List["str"]] = {
            "bake": [
                "flour",
                "sugar",
                "butter",
                "eggs",
                "vanilla extract",
                "chocolate",
                "baking powder",
                "cocoa powder",
            ],
            "grill": [
                "steak",
                "chicken",
                "vegetables",
                "marinade",
                "olive oil",
                "spices",
                "barbecue sauce",
            ],
            "saute": [
                "onion",
                "garlic",
                "mushroom",
                "butter",
                "olive oil",
                "white wine",
                "herbs",
            ],
            "boil": [
                "pasta",
                "eggs",
                "potatoes",
                "water",
                "salt",
                "sauce",
                "vegetables",
                "rice",
            ],
            "simmer": [
                "stew meat",
                "vegetables",
                "broth",
                "tomatoes",
                "herbs",
                "wine",
                "onions",
            ],
            "fry": [
                "chicken",
                "fish",
                "potato",
                "oil",
                "flour",
                "breadcrumbs",
                "spices",
            ],
            "grill": [
                "steak",
                "chicken",
                "sausages",
                "vegetables",
                "marinade",
                "barbecue sauce",
                "charcoal",
            ],
            "roast": [
                "beef",
                "pork",
                "chicken",
                "lamb",
                "turkey",
                "marinade",
                "seasonings",
            ],
            "saute": [
                "onion",
                "garlic",
                "mushroom",
                "chicken",
                "shrimp",
                "white wine",
                "butter",
            ],
            "steam": [
                "broccoli",
                "asparagus",
                "carrots",
                "rice",
                "fish",
                "steamed buns",
                "vegetables",
            ],
            "chop": [
                "vegetables",
                "herbs",
                "nuts",
                "fruits",
                "meat",
                "garlic",
                "onion",
            ],
            "dice": ["onion", "celery", "carrots", "potatoes", "bell pepper", "tomato"],
            "mince": ["garlic", "shallots", "onion", "ginger", "herbs", "meat"],
            "slice": ["onion", "bell pepper", "cucumber", "tomato", "bread", "meat"],
            "grate": [
                "cheese",
                "carrots",
                "zucchini",
                "potatoes",
                "lemon zest",
                "Parmesan",
            ],
            "peel": [
                "potatoes",
                "carrots",
                "apples",
                "citrus fruits",
                "ginger",
                "kiwi",
            ],
            "trim": [
                "fat from meat",
                "ends of green beans",
                "artichokes",
                "asparagus",
                "excess skin from chicken",
            ],
            "shred": ["cheese", "cabbage", "carrots", "zucchini", "potatoes", "radish"],
            "stir": ["sauce", "soup", "risotto", "stew", "rice", "pasta", "porridge"],
            "whisk": [
                "eggs",
                "batter",
                "sauce",
                "dressing",
                "cream",
                "meringue",
                "pancake mix",
            ],
            "blend": ["smoothies", "soups", "sauces", "dips", "milkshakes", "batters"],
            "fold": [
                "egg whites",
                "cream",
                "chocolate chips",
                "nuts",
                "berries",
                "whipped cream",
            ],
            "knead": [
                "bread dough",
                "pizza dough",
                "pastry dough",
                "cookies",
                "bagels",
                "pretzels",
            ],
            "measure": ["flour", "sugar", "water", "oil", "spices", "butter", "milk"],
            "serve": [
                "plating",
                "garnishing",
                "serving utensils",
                "serving plates",
                "napkins",
            ],
            "prep": [
                "vegetables",
                "meat",
                "fruits",
                "ingredients",
                "cleaning",
                "washing",
                "cutting",
                "peeling",
            ],
        }
        return action_ingredient_map

    def create_action_tool_map(self) -> Dict["str", List["str"]]:
        """
        Create a dictionary that maps cooking actions to the list of cooking tools typically used for each action.

        Returns:
        - Dict[str, List[str]]: A dictionary where keys are cooking actions and values are lists of associated cooking tools.
        """
        action_tool_map: Dict["str", List["str"]] = {
            "bake": [
                "oven",
                "baking sheet",
                "rolling pin",
                "muffin tin",
                "cake pan",
                "cookie cutter",
                "pastry brush",
                "baking stone",
                "pie dish",
                "bread pan",
            ],
            "grill": [
                "grill",
                "tongs",
                "grill brush",
                "basting brush",
                "smoker box",
                "grill basket",
                "skewers",
                "heat-resistant gloves",
                "instant-read thermometer",
                "grill grates",
            ],
            "saute": ["skillet", "spatula", "saucepan"],
            "boil": ["pot", "saucepan", "strainer"],
            "simmer": ["pot", "saucepan", "stockpot", "Dutch oven", "casserole dish"],
            "fry": [
                "skillet",
                "pan",
                "pot",
                "deep fryer",
                "wok",
                "tongs",
                "spider strainer",
            ],
            "grill": [
                "grill",
                "barbecue",
                "smoker",
                "grill pan",
                "tongs",
                "grill brush",
                "basting brush",
                "skewers",
                "heat-resistant gloves",
                "instant-read thermometer",
            ],
            "roast": ["roasting pan", "oven", "baking sheet", "meat thermometer"],
            "saute": ["skillet", "saucepan", "saute pan", "wok", "spatula"],
            "steam": ["steamer", "steamer basket", "saucepan", "bamboo steamer"],
            "chop": ["knife", "chef's knife", "cleaver", "paring knife", "mezzaluna"],
            "dice": ["knife", "chef's knife", "cleaver", "paring knife", "mezzaluna"],
            "mince": ["knife", "chef's knife", "cleaver", "paring knife", "mezzaluna"],
            "slice": [
                "knife",
                "chef's knife",
                "bread knife",
                "slicing knife",
                "utility knife",
            ],
            "grate": ["grater", "microplane", "box grater"],
            "peel": ["peeler", "paring knife"],
            "trim": ["kitchen shears", "knife", "paring knife", "scissors"],
            "shred": ["box grater", "mandoline", "food processor", "knife"],
            "stir": ["spoon", "wooden spoon", "spatula", "whisk", "mixing spoon"],
            "whisk": ["whisk", "fork", "electric mixer"],
            "blend": ["blender", "food processor", "immersion blender", "stand mixer"],
            "fold": ["spatula", "wooden spoon"],
            "knead": ["hands", "kneading surface"],
            "measure": ["measuring cups", "measuring spoons", "kitchen scale"],
            "serve": ["serving utensils", "plates", "platters", "silverware"],
            "prep": ["knife", "cutting board", "peeler", "paring knife", "scissors"],
        }
        return action_tool_map

    def get_action_ingredient_map(self) -> Dict["str", List["str"]]:
        """
        Get the dictionary that maps cooking actions to associated ingredients.

        Returns:
        - Dict[str, List[str]]: A dictionary where keys are cooking actions and values are lists of associated ingredients.
        """
        return self.action_ingredient_map

    def get_action_tool_map(self) -> Dict["str", List["str"]]:
        """
        Get the dictionary that maps cooking actions to associated cooking tools.

        Returns:
        - Dict[str, List[str]]: A dictionary where keys are cooking actions and values are lists of associated cooking tools.
        """
        return self.action_tool_map

    def find_ingredients_for_action(self, action):
        """
        Returns a list of ingredients typically used for the given cooking action.

        Parameters:
        - action (str): The cooking action for which ingredients are needed.

        Returns:
        - List[str]: A list of ingredients commonly associated with the provided cooking action.
        """
        return self.get_action_ingredient_map().get(action, [])

    def find_tools_for_action(self, action):
        """
        Returns a list of cooking tools typically used for the given cooking action.

        Parameters:
        - action (str): The cooking action for which cooking tools are needed.

        Returns:
        - List[str]: A list of cooking tools commonly associated with the provided cooking action.
        """
        return self.get_action_tool_map().get(action, [])
