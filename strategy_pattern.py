class HappyHourStrategy(object):

    def apply_discount(self, price):
        return price * 0.5


class NormalStrategy(object):

    def apply_discount(self, price):
        return price


class Bill(object):
    lines = []

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def add(self, price, quantity):
        self.lines.append(self.strategy.apply_discount(price) * quantity)

    def sum(self):
        return sum(self.lines)


bill = Bill(NormalStrategy())
bill.add(10, 2)
bill.set_strategy(HappyHourStrategy())
bill.add(10, 2)
print bill.sum()
