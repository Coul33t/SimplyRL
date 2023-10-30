import tcod

import random as rn
import numpy as np

from systems.sys_template import *
from game_map import *

from constants import (DUNGEON_DISPLAY_WIDTH,
                       DUNGEON_DISPLAY_HEIGHT)

FOV_ALGO = 0
FOV_LIGHT_WALLS = True

#TODO: Merge sys_map.py with game_map.py

class SysMap(SysTemplate):
    def __init__(self):
        super().__init__()

        self.game_map = GameMap(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT)
        self._fov_map = tcod.map.Map(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT, 'F')
        self._fov_recompute = True

        self._a_star = tcod.path.AStar(self._fov_map)

        self._current_map_level = 1
        self.visible_tiles = []


    def new_map(self):
        coordinates = self.game_map.create_map()
        self.populate_dungeon()
        return coordinates

    def init_fov(self):
        self._fov_recompute = True

        for x in range(self._fov_map.width):
            for y in range(self._fov_map.height):
                self._fov_map.transparent[x, y] = not self.game_map.map_array[x][y].block_sight
                self._fov_map.walkable[x, y] = not self.game_map.map_array[x][y].blocked


    def create_monster(self, x, y, ch='X', fg='green', bg=None):
        monster = self.entity_manager.create_entity()
        self.entity_manager.add_component(monster, 'Physics', x=x, y=y, blocks_sight=False)
        self.entity_manager.add_component(monster, 'Graphics', name='Basic Monster', ch=ch, fg=fg, bg=bg)
        self.entity_manager.add_component(monster, 'Stats', hp=10)
        self.entity_manager.add_component(monster, 'Ai')
        self.entity_manager.add_component(monster, 'Interactions', can_be_interacted=['attack'])


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

        p_phys = self.entity_manager.get_system('Physics').get_component(self.entity_manager.get_entity_by_tag('Player'))
        p_vis = self.entity_manager.get_system('Stats').get_component(self.entity_manager.get_entity_by_tag('Player')).vision_range

        self._fov_map.compute_fov(p_phys.x, p_phys.y, radius=p_vis, light_walls=FOV_LIGHT_WALLS)
        self.visible_tiles = np.ndarray.tolist(np.array(np.where(self._fov_map.fov==True)).T)

        for coord in self.visible_tiles:
            coord.reverse()
        

    def update(self):
        self.compute_visible_tiles()
