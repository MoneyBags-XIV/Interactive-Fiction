from random import choice

generic_sass = ['Don\'t be silly.',
    'Pull yourself together!',
    'Nice try.',
    'Behave yourself!',
    'And they call humans sophisticated.',
    'Oh please.',
    'Seriously!?!'
]

def hit():
    print('Killed.')

def take():
    print('Taken.')

def go():
    print('Gone')

verbs = {'hit': hit,
    'kill': hit,
    'smack': hit,
    'kick': hit,
    'take': take,
    'go': go
}