import unittest
from coffee_shop import CoffeeShop


class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        """Этот метод запускается перед каждым тестом"""
        self.shop = CoffeeShop()

    def test_sell_espresso(self):
        """Тест: продажа эспрессо"""
        result = self.shop.sell_espresso()
        self.assertEqual(result, "Эспрессо готов!")
        self.assertEqual(self.shop.get_balance(), 100)
        self.assertEqual(self.shop.get_cups_sold(), 1)

    def test_sell_americano(self):
        """Тест: продажа американо"""
        result = self.shop.sell_americano()
        self.assertEqual(result, "Американо готов!")
        self.assertEqual(self.shop.get_balance(), 120)
        self.assertEqual(self.shop.get_cups_sold(), 1)

    def test_not_enough_water(self):
        """Тест: не хватает воды"""
        # Тратим всю воду
        self.shop.water = 10
        result = self.shop.sell_espresso()
        self.assertEqual(result, "Не хватает воды!")
        self.assertEqual(self.shop.get_balance(), 0)

    def test_not_enough_beans(self):
        """Тест: не хватает зёрен"""
        # Тратим все зёрна
        self.shop.beans = 5
        result = self.shop.sell_espresso()
        self.assertEqual(result, "Не хватает зёрен!")
        self.assertEqual(self.shop.get_balance(), 0)

    def test_multiple_sales(self):
        """Тест: несколько продаж подряд"""
        self.shop.sell_espresso()
        self.shop.sell_espresso()
        self.shop.sell_americano()

        self.assertEqual(self.shop.get_balance(), 320)  # 100 + 100 + 120
        self.assertEqual(self.shop.get_cups_sold(), 3)


if __name__ == '__main__':
    unittest.main()