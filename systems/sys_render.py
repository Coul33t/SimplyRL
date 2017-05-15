from components.graphics import Graphics
from systems.sys_template import *

class SysRender(SysTemplate):
    def __init__(self, terminal, game_map):
        self._component_list = OrderedDict()
        self._game_map = game_map
        self._terminal = terminal
        self._entity_manager = None

    def create_component(self, entity, **params):
        self._component_list[entity] = Graphics(**params)

    def set_ref_to_entity_manager(self, manager):
        self._entity_manager = manager

    def update(self):
        # Display reset
        self._terminal.bkcolor('black')
        self._terminal.clear()

        # Map drawing
        self._terminal.layer(0)

        for i in range(0, self._game_map.width):
            for j in range(0, self._game_map.height):
                self._terminal.color(self._game_map.map_array[i][j].fg)
                self._terminal.bkcolor(self._game_map.map_array[i][j].bg)
                self._terminal.puts(i, j, self._game_map.map_array[i][j].ch)

        # Entities drawing
        self._terminal.layer(1)

        # Code readability
        manager = self._entity_manager

        # For every entity which has a Render component
        for elem in self._component_list:

            if self._component_list[elem].fg:
                self._terminal.color(self._component_list[elem].fg)

            if self._component_list[elem].bg:
                self._terminal.bkcolor(self._component_list[elem].bg)

            # Code readability
            x = manager.get_system('Position').get_component(elem).x
            y = manager.get_system('Position').get_component(elem).y

            self._terminal.print(x, y, self._component_list[elem].ch)
