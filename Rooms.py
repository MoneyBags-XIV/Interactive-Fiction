class Room:
    def __init__(self, number, name, description, **directions):
        self.number = number
        self.name = name
        self.description = description
        self.directions = directions
        
    def move(self, direction):
        if direction in self.directions.keys():
            return self.directions[direction]
        
        else:
            return False