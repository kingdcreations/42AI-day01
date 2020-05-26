from datetime import datetime
from recipe import Recipe


class Book(object):
    """docstring for Book."""

    def __init__(self, name, last_update, creation_date, recipes):
        if not isinstance(name, str):
            self.ft_exit("Name must be a string")
        self.name = name
        if not isinstance(last_update, datetime):
            self.ft_exit("Last update must be a datetime")
        self.last_update = last_update
        if not isinstance(creation_date, datetime):
            self.ft_exit("Creation date must be a datetime")
        self.creation_date = creation_date
        if not isinstance(recipes, dict) or not len(recipes.keys()) == 3:
            self.ft_exit("Recipe list must be a dict of size 3")
        if not all(k in {"starter",  "lunch", "dessert"} for k in recipes):
            self.ft_exit("Recipe list must contain starter, lunch and dessert")
        self.recipes_list = recipes

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for x in self.recipes_list:
            for y in self.recipes_list[x]:
                if (y.name == name):
                    print(y)
                    return(y)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list:
            for x in self.recipes_list[recipe_type]:
                print(x)
                print()
        else:
            print("Recipe type does not exist")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        else:
            print("Recipe must be... a recipe!?")

    def ft_exit(self, s):
        print(s)
        exit()
