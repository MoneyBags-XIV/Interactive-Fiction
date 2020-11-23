import Parser
import Verbs
from random import choice

def main():
    place = 1
    Verbs.describe(place)
    while True:
        verb, noun, indirect, objection = Parser.parse(input('>>>'))
        if objection == 'none':
            if noun == indirect and noun != 'none':
                print(choice(Verbs.generic_sass))
            else:
                Verbs.verbs[verb](noun, indirect)
        else:
            print(objection)

if __name__ == '__main__':
    main()