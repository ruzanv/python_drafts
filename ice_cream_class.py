# class creates ice cream

class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles

    def add(self):
        dict_flavor = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5, 'Strawberry': 10, 'Chocolate': 10}
        return dict_flavor[self.flavor] + self.sprinkles