import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


@pytest.fixture()
def prepare_burger():
    mock = Mock()
    mock_price = mock.get_price.return_value = 30
    mock_name = mock.get_name.return_value = "булочка"
    bun = Bun(mock_name, mock_price)
    return bun


@pytest.fixture()
def prepare_ingredient():
    mock = Mock()
    mock_price = mock.get_price.return_value = 50
    mock_name = mock.get_name.return_value = "салат"
    mock_type = mock.get_type.return_value = "лук"
    ingredient = Ingredient(mock_type, mock_name, mock_price)
    return ingredient


@pytest.fixture()
def prepare_ingredients_to_append():
    mock = Mock()
    mock_price = mock.get_price.return_value = 50
    mock_name = mock.get_name.return_value = "салат"
    mock_type_1 = mock.get_type.return_value = "лук"
    mock_type_2 = mock.get_type.return_value = "чеснок"
    mock_type_3 = mock.get_type.return_value = "сыр"
    ingredient_1 = Ingredient(mock_type_1, mock_name, mock_price)
    ingredient_2 = Ingredient(mock_type_2, mock_name, mock_price)
    ingredient_3 = Ingredient(mock_type_3, mock_name, mock_price)
    ingredients = [ingredient_1, ingredient_2, ingredient_3]
    return ingredients



