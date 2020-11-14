import Items
import Verbs

def parse(input):
    case = input.lower()
    words = case.split(' ')
    verb = 'none'
    noun = 'none'
    indirect = 'none'
    objection = 'none'

    for word in words:
        for unnecessary in ['an', 'and', 'the', 'thee', 'a', 'of']:
            if word == unnecessary:
                del word

    for word in words:
        if word not in Verbs.verbs and Items.check_items(word) == False and word != 'using' and word != 'use' and word != 'with':
            objection = 'I don\'t know the word " ' + word + '."'
    
    if objection == 'none':
        for word in words:
            if word in Verbs.verbs:
                verb = word
                del word
                break
        
        if verb == 'none':
            objection = 'There\'s no verb in that sentence!'

        if objection == 'none':
            if 'using' or 'use' or 'with' in words:
                if words.count('using') + words.count('use') + words.count('with') > 1:
                    objection = 'I don\'t understand that sentence!'
                    
                else:
                    if 'using' in words:
                        indirect = words[words.index('using')+1]
                        del words[words.index('using')+1]
                        del words[words.index('using')]
                    elif 'use' in words:
                        indirect = words[words.index('use')+1]
                        del words[words.index('use')+1]
                        del words[words.index('use')]
                    elif 'with' in words:
                        indirect = words[words.index('with')+1]
                        del words[words.index('with')+1]
                        del words[words.index('with')]

            if objection == 'none':
                for word in words:
                    if Items.check_items(word) == True:
                        noun = word
                        del word
                        break

                if noun == 'none':
                    objection = 'There\'s no noun in that sentence!'
    
    return verb, noun, indirect, objection
