import random as rn

from engine import *

def main():
    engine = Engine()

    while engine.game_state is not 'exit':
        engine.update()
        terminal.refresh()

    terminal.close()

if __name__ == '__main__':
    main()
