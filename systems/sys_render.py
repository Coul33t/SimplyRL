from components.graphics import Graphics
from systems.sys_template import *

import pdb

class SysRender(SysTemplate):
    def __init__(self, terminal):
        super().__init__()
        self._terminal = terminal

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
    def _attenuate_color(self, color, ratio):
        if color:
            color = color.split(',')
            new_color = ''
            for channel in color:
                new_color += str(float(channel)*ratio) + ','

            return new_color[0:-1]

        return color

    def update(self):
        # Display reset
        self._terminal.bkcolor('black')
        self._terminal.clear()

        # Map drawing
        self._terminal.layer(0)

        game_map = self.entity_manager.get_system('Map').game_map

        for x in range(0, game_map.width):
            for y in range(0, game_map.height):

                if (x, y) in self.entity_manager.get_system('Map').visible_tiles:
                    game_map.map_array[x][y].explored = True
                    self._terminal.color(game_map.map_array[x][y].fg)
                    self._terminal.bkcolor(game_map.map_array[x][y].bg)
                    self._terminal.puts(x, y, game_map.map_array[x][y].ch)

                elif game_map.map_array[x][y].explored:
                    self._terminal.color(self._attenuate_color(game_map.map_array[x][y].fg, 0.25))
                    self._terminal.bkcolor(self._attenuate_color(game_map.map_array[x][y].bg, 0.25))
                    self._terminal.puts(x, y, game_map.map_array[x][y].ch)

        # Entities drawing
        self._terminal.layer(1)

        # For every entity which has a Render component
        for elem in self.component_list:
            e = self.entity_manager.get_system('Physics').get_component(elem)

            if (e.x, e.y) in self.entity_manager.get_system('Map').visible_tiles:
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
