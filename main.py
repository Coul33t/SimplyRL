from bearlibterminal import terminal
import pdb
import random as rn

from tile import *
from game_map import *

CHAR_TO_DRAW = {'w': ' ', 'f': ' '}
COLORS = {'w': '100,100,100', 'f': '150,150,150'}


def draw(g_map, entities):
    terminal.bkcolor('black') 
    terminal.clear()

    for i in range(0, g_map.width):
        for j in range(0, g_map.height):
            terminal.color(g_map.map_array[i][j].fgd_color)
            terminal.bkcolor(g_map.map_array[i][j].bkg_color)
            terminal.puts(i, j, g_map.map_array[i][j].ch)

    terminal.color('red')

    terminal.print(2, 2, '@')

def main():
    terminal.open()
    terminal.set("window.size=128x40, font: res/fonts/VeraMono.ttf, size=10x20")
    terminal.set("window.title='SimplyRL'")
    terminal.set("font: res/fonts/VeraMono.ttf, size=10x20")
    terminal.composition(True)
    terminal.refresh()

    g_map = GameMap()
    g_map.create_map()

    entities = []
     
    while terminal.read() != terminal.TK_CLOSE:
        draw(g_map, entities)
        terminal.refresh()
     
    terminal.close()

if __name__ == '__main__':
    main()
    