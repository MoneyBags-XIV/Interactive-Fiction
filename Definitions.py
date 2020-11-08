class Item:
    def __init__(self, names, breakable, deadly, portable=True, edible=False, drinkable=False,):
        self.names = names
        self.breakable = breakable
        self.deadly = deadly
        self.portable = portable
        self.edible = edible
        self.drinkable = drinkable