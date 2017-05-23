import tdl

import random as rn

from systems.sys_template import *
from game_map import *

import pdb

DUNGEON_DISPLAY_WIDTH = 50
DUNGEON_DISPLAY_HEIGHT = 15

FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 20

#TODO: Merge sys_map.py with game_map.py

class SysMap(SysTemplate):
    def __init__(self):
        self.game_map = GameMap(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT)
        self._fov_map = tdl.map.Map(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT)
        self._fov_recompute = True

        self._a_star = tdl.map.AStar(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT, self.move_cost, diagnalCost=1)

        self._current_map_level = 1
        self.visible_tiles = []


    def new_map(self):
        coordinates = self.game_map.create_map()
        self.populate_dungeon()
        return coordinates

    def init_fov(self):
        self._fov_recompute = True

        for x, y in self._fov_map:
            self._fov_map.transparent[x, y] = not self.game_map.map_array[x][y].block_sight
            self._fov_map.walkable[x, y] = not self.game_map.map_array[x][y].blocked


    def create_monster(self, x, y, ch='X', fg='green', bg=None):
        monster = self.entity_manager.create_entity()
        self.entity_manager.add_component(monster, 'Physics', x=x, y=y, blocks_sight=False)
        self.entity_manager.add_component(monster, 'Graphics', ch=ch, fg=fg, bg=bg)


    def populate_dungeon(self):
        for i in range(len(self.game_map.rooms)):
            nb = rn.randint(0,2)

            for _ in range(nb):
                x = rn.randint(self.game_map.rooms[i].x1+1, self.game_map.rooms[i].x2-1)
                y = rn.randint(self.game_map.rooms[i].y1+1, self.game_map.rooms[i].y2-1)

                self.create_monster(x, y)


    def is_blocked(self, x, y):
        if self.game_map.is_blocked(x, y):
            return True

        sys_physics = self.entity_manager.get_system('Physics')

        for entity in sys_physics.component_list:
            e = sys_physics.get_component(entity)

            if e.blocks and e.x == x and e.y == y:
                return True

        return False


    def move_cost(self, x, y):
        if self.game_map.is_blocked(x, y):
            return 0

        else:
            sys_physics = self.entity_manager.get_system('Physics')

            for entity in sys_physics.component_list:
                e = sys_physics.get_component(entity)

                if e.blocks and e.x == x and e.y == y:
                    return 10

        return 1


    def compute_visible_tiles(self):
        self.visible_tiles = []

        player = self.entity_manager.get_system('Physics').get_component(self.entity_manager.get_entity_by_tag('Player'))

        visible_tiles_iter = self._fov_map.compute_fov(player.x, player.y, radius=TORCH_RADIUS, light_walls=FOV_LIGHT_WALLS)

        for tile in visible_tiles_iter:
            self.visible_tiles.append(tile)


    def update(self):
        self.compute_visible_tiles()
