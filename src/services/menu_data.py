import csv

from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.load_data()

    def load_data(self) -> None:
        with open(self.source_path, "r") as file:
            csv_reader = csv.DictReader(file)
            unique_dishes = []

            for row in csv_reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                for dish in self.dishes:
                    if dish.name == dish_name:
                        ingredient = Ingredient(ingredient_name)
                        dish.add_ingredient_dependency(
                            ingredient, recipe_amount)

                if dish_name not in unique_dishes:
                    unique_dishes.append(dish_name)
                    current_dish = Dish(dish_name, dish_price)
                    self.dishes.add(current_dish)
                    ingredient = Ingredient(ingredient_name)
                    current_dish.add_ingredient_dependency(
                        ingredient, recipe_amount)
