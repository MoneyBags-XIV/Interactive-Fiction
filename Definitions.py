class Item:
    def __init__(self, names, description, breakable, deadly=False, portable=True, edible=False, drinkable=False, container=False):
        self.names = names
        self.description = description
        self.breakable = breakable
        self.deadly = deadly
        self.portable = portable
        self.edible = edible
        self.drinkable = drinkable
        self.container = container

    def __str__(self):
        return self.names

