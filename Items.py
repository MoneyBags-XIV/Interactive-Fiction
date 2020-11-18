class Item:
    def __init__(self, names, description, breakable=False, deadly=False, portable=True, edible=False, drinkable=False, container=False):
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

items = [
    Item(['thing', 'object'], 'This is a boring thing.', breakable=True),
    Item(['refrigerator', 'fridge'], 'This is an ordinary, white refrigerator.', breakble=False, portable=False, container=True)
]

def check_items(name):
    answer = False
    for i in range(len(items)):
        if name in items[i].names:
            answer = True
            break
    return answer