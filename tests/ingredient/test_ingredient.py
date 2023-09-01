from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    right_ingredient = Ingredient("queijo mussarela")
    wrong_ingredient = Ingredient("queijo parmesão")

    assert right_ingredient.name == "queijo mussarela"
    assert right_ingredient.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}

    assert right_ingredient.__eq__(right_ingredient) is True

    assert right_ingredient.__eq__(wrong_ingredient) is False

    assert right_ingredient.__hash__() == hash(right_ingredient.name)

    assert right_ingredient.__hash__() != hash(wrong_ingredient.name)

    assert right_ingredient.__repr__() == "Ingredient('queijo mussarela')"
