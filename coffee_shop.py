class CoffeeShop:
    def __init__(self):
        self.water = 1000  # мл
        self.beans = 500  # грамм
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

    def get_balance(self):
        """Вернуть текущий баланс"""
        return self.money

    def get_cups_sold(self):
        """Вернуть количество проданных чашек"""
        return self.total_cups