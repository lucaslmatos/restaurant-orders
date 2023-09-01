from src.models.dish import Dish  # noqa: F401, E261, E501
from typing import Dict

from src.models.ingredient import Ingredient
import pytest

Recipe = Dict[Ingredient, int]


# Req 2
def test_dish():
    right_dish = Dish("macarronada", 20.00)
    wrong_dish = Dish("feijoada", 25.00)
    right_ingredient = Ingredient("queijo mussarela")

    with pytest.raises(
            TypeError, match="Dish price must be float."):
        Dish("sandwiche de presunto", "10")

    with pytest.raises(
            ValueError, match="Dish price must be greater then zero."):
        Dish("pizza", -56.00)

    assert right_dish.name == "macarronada"

    assert right_dish.__eq__(right_dish) is True

    assert right_dish.__eq__(wrong_dish) is False

    assert right_dish.__hash__() == hash(right_dish.__repr__())

    assert right_dish.__hash__() != hash(wrong_dish.__repr__())

    assert right_dish.__repr__() == "Dish('macarronada', R$20.00)"

    right_dish.add_ingredient_dependency(right_ingredient, 5)

    assert right_dish.recipe == {right_ingredient: 5}

    assert right_dish.get_ingredients() == {right_ingredient}

    assert right_dish.get_restrictions() == right_ingredient.restrictions
