class Room:
    def __init__(self, name, description, **directions):
        self.name = name
        self.description = description
        self.directions = directions

    def go(self, direction):
        if direction in self.directions.keys():
            return self.directions[direction]
        
        else:
            return False

rooms = [
    Room('Inventory', 'This is the place where you carry things. Although, you can\t carry that many things since it\'s been a while since you\'ve been to the gym.'),
    Room('Room', 'This is a boring, ordinary room.', N=2),
    Room('Bigger Room', 'This room is just as boring, but it\'s a bit bigger.', S=1)
]