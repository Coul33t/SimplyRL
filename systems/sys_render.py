from components.graphics import Graphics
from systems.sys_template import *

import math

from constants import (MESSAGE_SIZE_X,
                       MESSAGE_SIZE_Y,
                       CONSOLE_SIZE_X,
                       CONSOLE_SIZE_Y,
                       STATS_PANEL_X,
                       STATS_PANEL_Y,
                       DUNGEON_DISPLAY_WIDTH,
                       DUNGEON_DISPLAY_HEIGHT)
import pdb

DEFAULT_MSG_BG_COLOUR = '0,0,0'
DEFAULT_MSG_FG_COLOUR = '255,255,255'

MAP_TILES = {'wall': ' ', 'floor': ' '}
MAP_TILES_ASCII = {'wall': '#', 'floor': '.'}

HP_COLOURS = {'good': ['75,255,75', '20,80,20'], 'med': ['255,100,0', '15,50,0'], 'bad': ['255,0,0', '150,0,0']}

class SysRender(SysTemplate):
    def __init__(self, terminal):
        super().__init__()
        self._terminal = terminal
        self.display_type = 1

    def create_component(self, entity, **params):
        self.component_list[entity] = Graphics(**params)

    '''
        Used to attenuate a color by a ratio (between 0 and 1).
        Input :
                color : a rgb color, as a string (e.g. : '255,255,0')
                ratio : the ratio (e.g. : 0.5)
        Output :
                the modified color, as a string (e.g. : '127,127,0')
    '''
    def _attenuate_color(self, colour, ratio):
        if colour:
            colour = colour.split(',')
            new_colour = ''
            for channel in colour:
                new_colour += str(int(float(channel)*ratio)) + ','

            return new_colour[0:-1]

        return colour

    def update(self):
        # Display reset
        self._terminal.bkcolor('black')
        self._terminal.clear()

        # Map drawing
        self._terminal.layer(0)

        game_map = self.entity_manager.get_system('Map').game_map
        visible_tiles = self.entity_manager.get_system('Map').visible_tiles

        for x in range(0, game_map.width):
            for y in range(0, game_map.height):

                if [x, y] in visible_tiles:
                    game_map.map_array[x][y].explored = True
                    # NO ASCII
                    if self.display_type == 1:
                        self._terminal.color(game_map.map_array[x][y].fg)
                        self._terminal.bkcolor(game_map.map_array[x][y].bg)
                        self._terminal.puts(x, y, ' ')
                    else:
                        self._terminal.color(game_map.map_array[x][y].bg)
                        self._terminal.bkcolor('0,0,0')
                        self._terminal.puts(x, y, game_map.map_array[x][y].ch)

                elif game_map.map_array[x][y].explored:
                    # NO ASCII
                    if self.display_type == 1:
                        self._terminal.color(self._attenuate_color(game_map.map_array[x][y].fg, 0.25))
                        self._terminal.bkcolor(self._attenuate_color(game_map.map_array[x][y].bg, 0.25))
                        self._terminal.puts(x, y, ' ')
                    else:
                        self._terminal.color(self._attenuate_color(game_map.map_array[x][y].bg, 0.25))
                        self._terminal.bkcolor('0,0,0')
                        self._terminal.puts(x, y, game_map.map_array[x][y].ch)


        # Entities drawing
        self._terminal.layer(1)

        # For every entity which has a Render component
        for elem in self.component_list:
            e = self.entity_manager.get_system('Physics').get_component(elem)

            if (e.x, e.y) in visible_tiles:
                self.component_list[elem].last_seen = [e.x, e.y]

                if self.component_list[elem].fg:
                    self._terminal.color(self.component_list[elem].fg)

                if self.component_list[elem].bg:
                    self._terminal.bkcolor(self.component_list[elem].bg)

                self._terminal.print(e.x, e.y, self.component_list[elem].ch)

            elif not None in self.component_list[elem].last_seen:
                if self.component_list[elem].fg:
                    self._terminal.color('darker ' + self.component_list[elem].fg)

                if self.component_list[elem].bg:
                    self._terminal.bkcolor('darker ' + self.component_list[elem].bg, 0.25)

                self._terminal.print(e.x, e.y, self.component_list[elem].ch)


        # Message drawing
        self._terminal.layer(0)
        self._terminal.bkcolor(DEFAULT_MSG_BG_COLOUR)
        for x in range(0, MESSAGE_SIZE_X):
            for y in range(CONSOLE_SIZE_Y - MESSAGE_SIZE_Y, CONSOLE_SIZE_Y):
                self._terminal.puts(x, y, ' ')

        messages = self.entity_manager.get_system('Messages').return_msg(MESSAGE_SIZE_Y)
        if messages:
            y = CONSOLE_SIZE_Y - 1
            for i,msg in enumerate(messages):

                fg_col = DEFAULT_MSG_FG_COLOUR
                if  msg.fg_colour:
                    fg_col = self._attenuate_color(msg.fg_colour, 1-(i/MESSAGE_SIZE_Y))

                self._terminal.color(fg_col)

                bg_col = DEFAULT_MSG_BG_COLOUR
                if msg.bg_colour:
                    bg_col = self._attenuate_color(msg.bg_colour, 1-(i/MESSAGE_SIZE_Y))

                self._terminal.bkcolor(bg_col)

                self._terminal.print(0, y, f'{msg.txt}')
                y -= 1

        # Player stats drawing
        hp_colours = HP_COLOURS['good']
        player = self.entity_manager.get_system('Stats').get_component(self.entity_manager.get_entity_by_tag('Player'))
        if player.hp < player.max_hp/2:
            hp_colours = HP_COLOURS['med']
        if player.hp < player.max_hp/4:
            hp_colours = HP_COLOURS['bad']

        bar_total_width = STATS_PANEL_X - 2
        bar_value_width = math.ceil(float(player.hp) / player.max_hp * bar_total_width)

        y = 3

        for x in range(DUNGEON_DISPLAY_WIDTH + 1, CONSOLE_SIZE_X - 1):
            if (x - DUNGEON_DISPLAY_WIDTH - 1) <= bar_value_width:
                self._terminal.bkcolor(hp_colours[0])
                self._terminal.print(x, y, ' ')
            else:
                self._terminal.bkcolor(hp_colours[1])
                self._terminal.print(x, y, ' ')


