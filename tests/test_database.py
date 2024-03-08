from praktikum.database import Database


class TestDataBase:
    def test_available_buns(self):
        data_base = Database()
        assert data_base.buns == data_base.available_buns()

    def test_available_ingredients(self):
        data_base = Database()
        assert data_base.ingredients == data_base.available_ingredients()


