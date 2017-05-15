import pdb
import random as rn

from engine import *

CHAR_TO_DRAW = {'w': ' ', 'f': ' '}
COLORS = {'w': '100,100,100', 'f': '150,150,150'}


#TODO: check relevance of mutators in classes

def main():
    engine = Engine()

    #engine.init()

    while True:
        engine.update()
        #engine.draw()
        #engine.handling_keys()
        terminal.refresh()

    terminal.close()

if __name__ == '__main__':
    main()
