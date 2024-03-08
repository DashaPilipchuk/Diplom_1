from praktikum.bun import Bun
import pytest
from unittest.mock import Mock


class TestBun:
    @pytest.mark.parametrize('name', ['Флюоресцентная булка', 'Краторная булка', 'с кунжутом'])
    def test_get_name(self, name):
        mock_price = Mock()
        mock_price.get_price.return_value = 30
        bun = Bun(name, mock_price)
        assert bun.get_name() == bun.name

    @pytest.mark.parametrize('price', [30, 20.5, 1])
    def test_get_price(self, price):
        mock_name = Mock()
        mock_name.get_name.return_value = "с орехами"
        bun = Bun(mock_name, price)
        assert bun.get_price() == bun.price
