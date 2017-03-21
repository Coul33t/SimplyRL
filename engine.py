from bearlibterminal import terminal
import tdl

from game_map import *
from player import *



DUNGEON_DISPLAY_WIDTH = 50
DUNGEON_DISPLAY_HEIGHT = 15

class Engine:
    def __init__(self):
        self._game_map = GameMap(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT)
        self._fov_map = tdl.map.Map(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT)
        self._fov_recompute = True

        self._a_star = tdl.map.AStar(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT, self.move_cost, diagnalCost=1)

        self._current_map_level = 1

        self._entities = []
        self._objects = []
        self._visible_tiles = []
        
        self._game_state = 'main_menu'

        self._player = Player(-1, -1, '@', fg='red')
        self._player_action = 'didnt_take_turn'


    def init(self):
        self.init_terminal()

        (self._player.x, self._player.y) = self._game_map.create_map()
        
        self.init_fov()

        self._game_state = 'playing'


    def init_fov(self):
        self._fov_recompute = True

        for x, y in self._fov_map:
            self._fov_map.transparent[x, y] = not self._game_map.map_array[x][y].block_sight
            self._fov_map.walkable[x, y] = not self._game_map.map_array[x][y].blocked


    def init_terminal(self):
        terminal.open()
        terminal.set("window.size=64x20, font: res/fonts/VeraMono.ttf, size=10x20")
        terminal.set("window.title='SimplyRL'")
        terminal.set("font: res/fonts/VeraMono.ttf, size=20x40")
        terminal.composition(True)
        terminal.refresh()


    def handling_keys(self):
        key = terminal.read()

        terminal.puts(10,10, '[color=orange]{}[/color]'.format(key))


    def is_blocked(self, x, y):
        if self._game_map.is_blocked(x, y):
            return True

        for entity in self._entities:
            if entity.blocks and entity.x == x and entity.y == y:
                return True


    def move_cost(self, x, y):
        if self._game_map.is_blocked(x, y):
            return 0

        else:
            for entity in self._entities:
                if entity.blocks and entity.x == x and entity.y == y:
                    return 10

        return 1


    def send_to_back(self, entity):
        self._entities.remove(entity)
        self._entities.insert(0, entity)


    def draw(self):
        terminal.bkcolor('black')
        terminal.clear()

        terminal.layer(0)

        for i in range(0, self._game_map.width):
            for j in range(0, self._game_map.height):
                terminal.color(self._game_map.map_array[i][j].fg)
                terminal.bkcolor(self._game_map.map_array[i][j].bg)
                terminal.puts(i, j, self._game_map.map_array[i][j].ch)

        terminal.layer(1)

        for entity in self._entities:
            if entity.fg:
                terminal.color(entity.fg)

            if entity.bg:
                terminal.bkcolor(entity.bg)

            terminal.print(entity.x, entity.y, entity.ch)

        terminal.layer(2)

        if self._player.fg:
            terminal.color(self._player.fg)

        if self._player.bg:
            terminal.bkcolor(self._player.bg)

        terminal.print(self._player.x, self._player.y, self._player.ch)