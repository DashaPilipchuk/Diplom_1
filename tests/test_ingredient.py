from unittest.mock import Mock
from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    @pytest.mark.parametrize('price', [30, 20.5, 1])
    def test_get_price(self, price):
        mock = Mock()
        mock_name = mock.get_name.return_value = "салат"
        mock_type = mock.get_type.return_value = "лук"
        ingredient = Ingredient(mock_type, mock_name, price)
        assert ingredient.get_price() == ingredient.price

    @pytest.mark.parametrize('name', ['томат', 'чеснок', 'кунжут'])
    def test_get_name(self, name):
        mock = Mock()
        mock_price = mock.get_price.return_value = 50.1
        mock_type = mock.get_type.return_value = "булка"
        ingredient = Ingredient(mock_type, name, mock_price)
        assert ingredient.get_name() == ingredient.name

    @pytest.mark.parametrize('type', ['овощи', 'фрукты', 'соус'])
    def test_get_type(self, type):
        mock = Mock()
        mock_price = mock.get_price.return_value = 10.5
        mock_name = mock.get_name.return_value = "салат"
        ingredient = Ingredient(type, mock_name, mock_price)
        assert ingredient.get_type() == ingredient.type

