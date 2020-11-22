from random import choice

generic_sass = ['Don\'t be silly.',
    'Pull yourself together!',
    'Nice try.',
    'Behave yourself!',
    'Oh please.',
    'Seriously!?!',
    'So uncivilized.',
    'You can\'t do that!'
]

def find_indirect(verb, noun):
    indirect = input('What do you want to '+verb+' the '+noun+' with?\n>>>')
    return indirect

def find_noun(verb):
    noun = input('What do you want to '+verb+'?')
    return noun

def hit(noun, indirect):
    print('Killed.')

def take(noun, indirect):
    print('Taken.')

def go(noun, indirect):
    print('Gone.')

verbs = {'hit': hit,
    'kill': hit,
    'smack': hit,
    'kick': hit,
    'take': take,
    'go': go
}