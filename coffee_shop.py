class CoffeeShop:
    def __init__(self):
        self.water = 1000  # мл
        self.beans = 500  # грамм
        self.milk = 500  # мл
        self.chocolate = 200  # грамм
        self.money = 0  # рублей
        self.total_cups = 0

    def sell_espresso(self):
        """Продать эспрессо (30 мл воды, 15 г зёрен, 100 рублей)"""
        if self.water < 30:
            return "Не хватает воды!"
        if self.beans < 15:
            return "Не хватает зёрен!"

        self.water -= 30
        self.beans -= 15
        self.money += 100
        self.total_cups += 1
        return "Эспрессо готов!"

    def sell_americano(self):
        """Продать американо (100 мл воды, 15 г зёрен, 120 рублей)"""
        if self.water < 100:
            return "Не хватает воды!"
        if self.beans < 15:
            return "Не хватает зёрен!"

        self.water -= 100
        self.beans -= 15
        self.money += 120
        self.total_cups += 1
        return "Американо готов!"

    def sell_latte(self):
        """Продать латте (200 мл воды, 20 г зёрен, 15 г молока, 150 рублей)"""
        if self.water < 200:
            return "Не хватает воды!"
        if self.beans < 20:
            return "Не хватает зёрен!"
        if self.milk < 15:
            return "Не хватает молока!"

        self.water -= 200
        self.beans -= 20
        self.milk -= 15
        self.money += 150
        self.total_cups += 1
        return "Латте готов!"

    def sell_cappuccino(self):
        """Продать капучино (150 мл воды, 18 г зёрен, 20 г молока, 140 рублей)"""
        if self.water < 150:
            return "Не хватает воды!"
        if self.beans < 18:
            return "Не хватает зёрен!"
        if self.milk < 20:
            return "Не хватает молока!"

        self.water -= 150
        self.beans -= 18
        self.milk -= 20
        self.money += 140
        self.total_cups += 1
        return "Капучино готов!"

    def sell_mocha(self):
        """Продать мокко (100 мл воды, 15 г зёрен, 10 г шоколада, 180 рублей)"""
        if self.water < 100:
            return "Не хватает воды!"
        if self.beans < 15:
            return "Не хватает зёрен!"
        if self.chocolate < 10:
            return "Не хватает шоколада!"

        self.water -= 100
        self.beans -= 15
        self.chocolate -= 10
        self.money += 180
        self.total_cups += 1
        return "Мокко готов!"

    def get_balance(self):
        """Вернуть текущий баланс"""
        return self.money

    def get_cups_sold(self):
        """Вернуть количество проданных чашек"""
        return self.total_cups