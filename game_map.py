from tile import *
from tools import rnd_color
from tools import Rect

import random as rn
import math

MAP_TILES = {'wall': ' ', 'floor': ' '}
COLORS = {'wall': '50,50,50', 'floor': '225,225,225'}

MIN_ROOM = 2
MAX_ROOM = 10
MIN_ROOM_SIZE = 3
MAX_ROOM_SIZE = 7

class GameMap:
    def __init__(self, width=40, height=20):
        self._width = width
        self._height = height
        self._map_array = [[Tile(ch=MAP_TILES['wall'], fg=None, bg=COLORS['wall']) for x in range(height)] for y in range(width)]
        self._rooms = []

    def _get_width(self):
        return self._width

    def _set_width(self, width):
        self._width = width

    width = property(_get_width, _set_width)

    def _get_height(self):
        return self._height

    def _set_height(self, height):
        self._height = height

    height = property(_get_height, _set_height)

    def _get_map_array(self):
        return self._map_array

    def _set_map_array(self, map_array):
        self._map_array = map_array

    map_array = property(_get_map_array, _set_map_array)

    def _get_rooms(self):
        return self._rooms

    def _set_rooms(self, rooms):
        pass

    rooms = property(_get_rooms, _set_rooms)


    def clear_map(self):
        self._map_array = [[Tile(ch=MAP_TILES['wall'], fg=None, bg=COLORS['wall']) for x in range(0,self._height)] for y in range(0,self._width)]


    def create_room(self, room):
        for x in range(room.x1, room.x2):
            for y in range(room.y1, room.y2):
                self._map_array[x][y].ch = MAP_TILES['floor']
                self._map_array[x][y].bg = rnd_color(COLORS['floor'],[0.05,0.05,0.05], same=True)
                self._map_array[x][y].blocked = False
                self._map_array[x][y].block_sight = False

    def carve_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self._map_array[x][y].ch = MAP_TILES['floor']
            self._map_array[x][y].bg = rnd_color(COLORS['floor'],[0.05,0.05,0.05], same=True)
            self._map_array[x][y].blocked = False
            self._map_array[x][y].block_sight = False

    def carve_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self._map_array[x][y].ch = MAP_TILES['floor']
            self._map_array[x][y].bg = rnd_color(COLORS['floor'],[0.05,0.05,0.05], same=True)
            self._map_array[x][y].blocked = False
            self._map_array[x][y].block_sight = False


    def create_map(self, max_room=MAX_ROOM, min_room=MIN_ROOM, min_room_size=MIN_ROOM_SIZE, max_room_size=MAX_ROOM_SIZE):
        num_rooms = 0

        self.clear_map()

        while num_rooms < max_room:

            if num_rooms >= min_room:
                if rn.random() <= (num_rooms - min_room)/(max_room - min_room):
                    break

            carved = False

            while not carved:

                carved = True

                w = rn.randint(min_room_size, max_room_size)
                h = rn.randint(min_room_size, max_room_size)
                x = rn.randint(1, self._width - w - 1)
                y = rn.randint(1, self._height - h - 1)

                new_room = Rect(x, y, w, h)

                if self._rooms:
                    for other_room in self._rooms:
                        if new_room.intersect(other_room):
                            carved = False
                else:
                    carved = True

            self.create_room(new_room)

            (new_x, new_y) = new_room.get_center()

            if num_rooms == 0:
                return_coordinates = (new_x, new_y)

            else:
                closest_room = [-1, -1]
                for i, other_room in enumerate(self._rooms):
                    if closest_room == [-1, -1]:
                        closest_room = list(other_room.get_center())
                    else:
                        if math.sqrt(pow(other_room.x1 - x, 2) + pow(other_room.y1 - y, 2)) < math.sqrt(pow(closest_room[0] - x, 2) + pow(closest_room[1] - y, 2)):
                            closest_room = list(other_room.get_center())

                if rn.random() > 0.5:
                    self.carve_h_tunnel(x, closest_room[0], y)
                    self.carve_v_tunnel(y, closest_room[1], closest_room[0])
                else:
                    self.carve_v_tunnel(y, closest_room[1], x)
                    self.carve_h_tunnel(x, closest_room[0], closest_room[1])


            self._rooms.append(new_room)

            num_rooms += 1

        return return_coordinates
