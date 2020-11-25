import Rooms
import Items
from random import choice

generic_sass = ['Don\'t be silly.',
    'Pull yourself together!',
    'Nice try.',
    'Behave yourself!',
    'Oh please.',
    'Seriously!?!',
    'So uncivilized.',
    'You can\'t do that!',
    'Good luck.'
]




def find_indirect(verb, noun):
    indirect = input('What do you want to '+verb+' the '+noun+' with?\n>>>')
    return indirect

def find_noun(verb):
    noun = input('What do you want to '+verb+'?')
    return noun

def describe(place):
    print(Rooms.rooms[place].description)
    for thing in Items.items:
        if thing.location == place:
            print('The '+thing.names[0]+' is here.')




def hit(noun, indirect, place):
    print('Killed.')

def take(noun, indirect,place):
    print('Taken.')

def go(noun, indirect, place):
    print('Gone.')




verbs = {'hit': hit,
    'kill': hit,
    'smack': hit,
    'kick': hit,
    'take': take,
    'go': go
}