from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns(self, prepare_burger):
        burger = Burger()
        burger.set_buns(prepare_burger)
        assert prepare_burger == burger.bun

    def test_add_ingredient(self, prepare_ingredient):
        burger = Burger()
        burger.add_ingredient(prepare_ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients == [prepare_ingredient]

    def test_add_ingredients(self, prepare_ingredients_to_append):
        burger = Burger()
        burger.add_ingredient(prepare_ingredients_to_append[0])
        burger.add_ingredient(prepare_ingredients_to_append[1])
        burger.add_ingredient(prepare_ingredients_to_append[2])
        assert len(burger.ingredients) == 3 and burger.ingredients == [prepare_ingredients_to_append[0],
                                                                       prepare_ingredients_to_append[1],
                                                                       prepare_ingredients_to_append[2]]

    def test_remove_ingredient(self, prepare_ingredients_to_append):
        burger = Burger()
        burger.add_ingredient(prepare_ingredients_to_append[0])
        burger.add_ingredient(prepare_ingredients_to_append[1])
        burger.add_ingredient(prepare_ingredients_to_append[2])
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2 and burger.ingredients == [prepare_ingredients_to_append[0],
                                                                       prepare_ingredients_to_append[2]]

    def test_move_ingredient(self, prepare_ingredients_to_append):
        burger = Burger()
        burger.add_ingredient(prepare_ingredients_to_append[0])
        burger.add_ingredient(prepare_ingredients_to_append[1])
        burger.add_ingredient(prepare_ingredients_to_append[2])
        burger.move_ingredient(0,2)
        assert burger.ingredients[2] == prepare_ingredients_to_append[0]

    def test_get_price(self, prepare_burger, prepare_ingredient):
        burger = Burger()
        burger.bun = Bun(prepare_burger.name, prepare_burger.price)
        burger.ingredient = Ingredient(prepare_ingredient.type, prepare_ingredient.name, prepare_ingredient.price)
        burger.add_ingredient(prepare_ingredient)
        expected_price = prepare_burger.price * 2 + prepare_ingredient.price
        assert expected_price == burger.get_price()

    def test_get_receipt(self, prepare_burger, prepare_ingredient):
        burger = Burger()
        burger.bun = Bun(prepare_burger.name, prepare_burger.price)
        burger.ingredient = Ingredient(prepare_ingredient.type, prepare_ingredient.name, prepare_ingredient.price)
        burger.add_ingredient(prepare_ingredient)
        expected_receipt = (f'(==== {burger.bun.get_name()} ====)\n'
                            f'= {str(burger.ingredient.get_type()).lower()} {burger.ingredient.get_name()} =\n'
                            f'(==== {burger.bun.get_name()} ====)\n'
                            f'\nPrice: {burger.get_price()}')
        assert expected_receipt == burger.get_receipt()
