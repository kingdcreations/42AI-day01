class Recipe():
    """docstring for Book."""

    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, rt):
        if not name or not isinstance(name, str):
            self.ft_exit("Name must be a not empty string")
        self.name = name
        if not isinstance(cooking_lvl, int) or not 1 <= cooking_lvl <= 5:
            self.ft_exit("Cooking level must be a int between 1 and 5")
        self.cooking_lvl = int(cooking_lvl)
        if not isinstance(cooking_time, int) or cooking_time < 0:
            self.ft_exit("Cooking time must be a positive int")
        self.cooking_time = int(cooking_time)
        if not ingredients or not isinstance(ingredients, list):
            self.ft_exit("Ingredients must be a list of string")
        for x in ingredients:
            if not x or not isinstance(x, str):
                self.ft_exit("Ingredients must be a list of string")
        self.ingredients = ingredients
        if not isinstance(description, str):
            self.ft_exit("Description must be a string")
        self.description = description
        if not (rt == "starter" or rt == "lunch" or rt == "dessert"):
            self.ft_exit("Recipe type must be starter, lunch or dessert")
        self.recipe_type = rt

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += (f"Recipe for {self.name}:\n")
        txt += (f"Description:\n{self.description}\n")
        txt += (f"Cooking level: {self.cooking_lvl}\n")
        txt += (f"Ingredients list: {self.ingredients}\n")
        txt += (f"To be eaten for {self.recipe_type}\n")
        txt += (f"Takes {self.cooking_time} minutes of cooking.")
        return txt

    def ft_exit(self, s):
        print(s)
        exit()
