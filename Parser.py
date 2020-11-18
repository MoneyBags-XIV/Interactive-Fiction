import Items
import Verbs
from random import choice

def parse(input):
    case = input.lower()
    words = case.split(' ')
    verb = 'none'
    noun = 'none'
    indirect = 'none'
    objection = 'none'

    for i in range(len(words)-1, -1, -1):
        if words[i] in ['an', 'and', 'the', 'thee', 'a', 'of', 'to']:
            del words[i]

    for word in words:
        if word not in Verbs.verbs.keys() and Items.check_items(word) == False and word != 'using' and word != 'use' and word != 'with':
            objection = choice(['I don\'t know the word "' + word + '".', 'You can play this entire game, find every hidden secret, and get every posible point, without once using the word: "'+word+'".'])
    
    if objection == 'none':
        for word in words:
            if word in Verbs.verbs.keys():
                verb = word
                del word
                break
        
        if verb == 'none':
            objection = 'There\'s no verb in that sentence!'

        if objection == 'none':
            if 'using' or 'use' or 'with' in words:
                if words.count('using') + words.count('use') + words.count('with') > 1:
                    objection = 'I don\'t understand that sentence!'

                for thing in ['using', 'use', 'with']:
                    if thing in words:
                        if words.index(thing) + 2 > len(words):
                            objection = 'I don\'t understand that sentence!'

                if objection == 'none':
                    for thing in ['using', 'use', 'with']:
                        if thing in words:
                            indirect = words[words.index(thing)+1]
                            del words[words.index(thing)+1]
                            del words[words.index(thing)]

                    if objection == 'none':
                        for word in words:
                            if Items.check_items(word) == True:
                                noun = word
                                del word
                                break
        
    return verb, noun, indirect, objection
