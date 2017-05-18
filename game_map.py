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
        self.width = width
        self.height = height
        self.map_array = [[Tile(ch=MAP_TILES['wall'], fg=None, bg=COLORS['wall']) for x in range(height)] for y in range(width)]
        self.rooms = []


    def is_visible_tile(self, x, y):
        x = int(x)
        y = int(y)

        if x >= MAP_WIDTH or x < 0:
            return False

        elif y >= MAP_HEIGHT or y < 0:
            return False

        elif self._map_array[x][y].blocked:
            return False

        elif self._map_array[x][y].block_sight:
            return False

        else:
            return True

            

    def is_blocked(self, x, y):
        if self.map_array[x][y].blocked:
            return True

        return False




    def clear_map(self):
        self.map_array = [[Tile(ch=MAP_TILES['wall'], fg=None, bg=COLORS['wall']) for x in range(0,self.height)] for y in range(0,self.width)]


    def create_room(self, room):
        for x in range(room.x1, room.x2):
            for y in range(room.y1, room.y2):
                self.map_array[x][y].ch = MAP_TILES['floor']
                self.map_array[x][y].bg = rnd_color(COLORS['floor'],[0.05,0.05,0.05], same=True)
                self.map_array[x][y].blocked = False
                self.map_array[x][y].block_sight = False

    def carve_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map_array[x][y].ch = MAP_TILES['floor']
            self.map_array[x][y].bg = rnd_color(COLORS['floor'],[0.05,0.05,0.05], same=True)
            self.map_array[x][y].blocked = False
            self.map_array[x][y].block_sight = False

    def carve_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map_array[x][y].ch = MAP_TILES['floor']
            self.map_array[x][y].bg = rnd_color(COLORS['floor'],[0.05,0.05,0.05], same=True)
            self.map_array[x][y].blocked = False
            self.map_array[x][y].block_sight = False


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
                x = rn.randint(1, self.width - w - 1)
                y = rn.randint(1, self.height - h - 1)

                new_room = Rect(x, y, w, h)

                if self.rooms:
                    for other_room in self.rooms:
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
                for i, other_room in enumerate(self.rooms):
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


            self.rooms.append(new_room)

            num_rooms += 1

        return return_coordinates
