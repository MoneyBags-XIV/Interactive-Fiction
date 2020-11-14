import Parser

def main():
    while True:
        verb, noun, indirect, objection = Parser.parse(input('>>>'))
        if objection == 'none':
            print('verb: '+verb, '\nnoun: '+noun, '\nindirect: '+indirect)
        else:
            print(objection)

if __name__ == '__main__':
    main()