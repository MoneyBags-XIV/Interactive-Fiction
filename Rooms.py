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

rooms = [
    Room(0, 'Inventory', 'This is the place where you carry things. Although, you can\t carry that many things since it\'s been a while since you\'ve been to the gym.'),
    Room(1, 'Room', 'This is a boring, ordinary room.', N=2),
    Room(2, 'Bigger Room', 'This room is just as boring, but it\'s a bit bigger.', S=1)
]