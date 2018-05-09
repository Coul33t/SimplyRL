"""
    Python roguelike, made with BearLibTerminal, TDL and an ECS logic.
"""

from engine import (Engine, terminal)

def main():
    """
        The main loop of the program. Instanciates an Engine and loops
        until a quit signal is sent.
    """
    engine = Engine()

    while engine.game_state != 'exit':
        engine.update()
        terminal.refresh()

    terminal.close()

if __name__ == '__main__':
    main()
