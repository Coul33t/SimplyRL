import tdl

from systems.sys_template import *
from game_map import *

import pdb

DUNGEON_DISPLAY_WIDTH = 50
DUNGEON_DISPLAY_HEIGHT = 15

FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 20

class SysMap(SysTemplate):
    def __init__(self):
        self.game_map = GameMap(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT)
        self._fov_map = tdl.map.Map(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT)
        self._fov_recompute = True

        self._a_star = tdl.map.AStar(DUNGEON_DISPLAY_WIDTH, DUNGEON_DISPLAY_HEIGHT, self.move_cost, diagnalCost=1)

        self._current_map_level = 1
        self.visible_tiles = []

        self.init_fov()

    def init_fov(self):
        self._fov_recompute = True

        for x, y in self._fov_map:
            self._fov_map.transparent[x, y] = not self.game_map.map_array[x][y].block_sight
            self._fov_map.walkable[x, y] = not self.game_map.map_array[x][y].blocked


    def is_blocked(self, x, y):
        if self.game_map.is_blocked(x, y):
            return True

        sys_physics = self.entity_manager.get_system('Physics')

        for entity in sys_physics.component_list:
            if sys_physics.get_component(entity).blocks and sys_physics.get_component(entity).x == x and sys_physics.get_component(entity).y == y:
                return True

        return False


    def move_cost(self, x, y):
        if self.game_map.is_blocked(x, y):
            return 0

        else:
            sys_physics = self.entity_manager.get_system('Physics')
            for entity in sys_physics.component_list:
                if sys_physics.get_component(entity).blocks and sys_physics.get_component(entity).x == x and sys_physics.get_component(entity).y == y:
                    return 10

        return 1


    def compute_visible_tiles(self):

        self.visible_tiles = []

        player = self.entity_manager.get_entity_by_tag('player')
        sys_position = self.entity_manager.get_system('Physics')

        visible_tiles_iter = self._fov_map.compute_fov(sys_position.get_component(player).x, sys_position.get_component(player).y, radius=TORCH_RADIUS, light_walls=FOV_LIGHT_WALLS)

        for tile in visible_tiles_iter:
            self.visible_tiles.append(tile)

        print(self.visible_tiles)

    def update(self):
        self.compute_visible_tiles()
