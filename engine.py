from bearlibterminal import terminal
import tdl

import pdb

from game_map import *
from player import *

from entities.entities_manager import *
from tags_manager import *

from systems.sys_input import *
from systems.sys_position import *
from systems.sys_event import *
from systems.sys_render import *

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

        self.init_terminal()

        self._entities_manager = EntityManager()

        self._entities_manager.subscribe_system(SysInput(terminal), 'Input')
        self._entities_manager.subscribe_system(SysPosition(), 'Position')
        self._entities_manager.subscribe_system(SysEvent(), 'Event')
        self._entities_manager.subscribe_system(SysRender(terminal, self._game_map), 'Graphics')

        (x_player, y_player) = self._game_map.create_map()

        self._player = self._entities_manager.create_entity()

        self._entities_manager.add_component(self._player, 'Position', x=x_player, y=y_player)
        self._entities_manager.add_component(self._player, 'Graphics', ch='@', fg='red', bg=None)

        self.init_fov()

        self._game_state = 'playing'

        self._entities_manager.associate_tag(self._player, 'player')


    def init(self):
        self.init_terminal()

        self._entities_manager.subscribe_system()

        (x_player, y_player) = self._game_map.create_map()
        self._entities_manager.add_component(self._player, 'Position', x=x_player, y=y_player)
        self._entities_manager.add_component(self._player, 'Graphics', ch='@', fg='red', bg=None)

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

        #if self._player.fg:
            #terminal.color(self._player.fg)

        #if self._player.bg:
            #terminal.bkcolor(self._player.bg)

        #terminal.print(self._player.x, self._player.y, self._player.ch)


    def update(self):
        for sys in self._entities_manager._systems_dict:
            print("{} system called".format(sys))
            self._entities_manager._systems_dict[sys].update()
