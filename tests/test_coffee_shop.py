import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

    def test_sell_latte(self):
        """Тест: продажа латте"""
        result = self.shop.sell_latte()
        self.assertEqual(result, "Латте готов!")
        self.assertEqual(self.shop.get_balance(), 150)
        self.assertEqual(self.shop.get_cups_sold(), 1)
        self.assertEqual(self.shop.water, 800)  # 1000 - 200
        self.assertEqual(self.shop.beans, 480)  # 500 - 20
        self.assertEqual(self.shop.milk, 485)  # 500 - 15

    def test_sell_cappuccino(self):
        """Тест: продажа капучино"""
        result = self.shop.sell_cappuccino()
        self.assertEqual(result, "Капучино готов!")
        self.assertEqual(self.shop.get_balance(), 140)
        self.assertEqual(self.shop.get_cups_sold(), 1)
        self.assertEqual(self.shop.water, 850)  # 1000 - 150
        self.assertEqual(self.shop.beans, 482)  # 500 - 18
        self.assertEqual(self.shop.milk, 480)  # 500 - 20

    def test_sell_mocha(self):
        """Тест: продажа мокко"""
        result = self.shop.sell_mocha()
        self.assertEqual(result, "Мокко готов!")
        self.assertEqual(self.shop.get_balance(), 180)
        self.assertEqual(self.shop.get_cups_sold(), 1)
        self.assertEqual(self.shop.water, 900)  # 1000 - 100
        self.assertEqual(self.shop.beans, 485)  # 500 - 15
        self.assertEqual(self.shop.chocolate, 190)  # 200 - 10

    def test_not_enough_milk(self):
        """Тест: не хватает молока"""
        # Тратим всё молоко
        self.shop.milk = 5
        result = self.shop.sell_latte()
        self.assertEqual(result, "Не хватает молока!")
        self.assertEqual(self.shop.get_balance(), 0)
        self.assertEqual(self.shop.get_cups_sold(), 0)

    def test_not_enough_chocolate(self):
        """Тест: не хватает шоколада"""
        # Тратим весь шоколад
        self.shop.chocolate = 5
        result = self.shop.sell_mocha()
        self.assertEqual(result, "Не хватает шоколада!")
        self.assertEqual(self.shop.get_balance(), 0)
        self.assertEqual(self.shop.get_cups_sold(), 0)

    def test_multiple_different_sales(self):
        """Тест: серия разных продаж"""
        self.shop.sell_espresso()
        self.shop.sell_latte()
        self.shop.sell_cappuccino()

        self.assertEqual(self.shop.get_balance(), 390)  # 100 + 150 + 140
        self.assertEqual(self.shop.get_cups_sold(), 3)


if __name__ == '__main__':
    unittest.main()