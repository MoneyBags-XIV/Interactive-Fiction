import Parser
import Verbs

def main():
    while True:
        verb, noun, indirect, objection = Parser.parse(input('>>>'))
        if objection == 'none':
            print('verb: '+verb, '\nnoun: '+noun, '\nindirect: '+indirect)
            Verbs.verbs[verb]()
        else:
            print(objection)

if __name__ == '__main__':
    main()