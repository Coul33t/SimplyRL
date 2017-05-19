from components.graphics import Graphics
from systems.sys_template import *

import pdb

class SysRender(SysTemplate):
    def __init__(self, terminal):
        super().__init__()
        self._terminal = terminal

    def create_component(self, entity, **params):
        self.component_list[entity] = Graphics(**params)

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
                    game_map[x][y].explored = True
                    self._terminal.color(game_map.map_array[x][y].fg)
                    self._terminal.bkcolor(game_map.map_array[x][y].bg)
                    self._terminal.puts(x, y, game_map.map_array[x][y].ch)
                elif game_map[x][y].explored:
                    self._terminal.color(game_map.map_array[x][y].fg)
                    self._terminal.bkcolor(game_map.map_array[x][y].bg)
                    self._terminal.puts(x, y, game_map.map_array[x][y].ch)

        # Entities drawing
        self._terminal.layer(1)

        # For every entity which has a Render component
        for elem in self.component_list:

            if self.component_list[elem].fg:
                self._terminal.color(self.component_list[elem].fg)

            if self.component_list[elem].bg:
                self._terminal.bkcolor(self.component_list[elem].bg)

            # Code readability
            x = self.entity_manager.get_system('Physics').get_component(elem).x
            y = self.entity_manager.get_system('Physics').get_component(elem).y

            self._terminal.print(x, y, self.component_list[elem].ch)
