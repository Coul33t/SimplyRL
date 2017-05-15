from components.position import Position
from systems.sys_template import *

MOVEMENT_KEYS = {93: [0, 0], 90: [0, 1], 89: [-1, 1], 92: [-1, 0], 95: [-1, -1], 96: [0, -1], 97: [1, -1],
                 94: [1, 0], 91: [1, 1]}

class SysInput(SysTemplate):
    def __init__(self, terminal=None):
        self._terminal = terminal
        self._entity_manager = None

    def update(self):
        key = self._terminal.read()
        print(key)

        if key is self._terminal.TK_CLOSE:
            self._terminal.close()

        if key in MOVEMENT_KEYS:
            self._entity_manager.get_system('Event').add_event(('Position', 'move', self._entity_manager.get_entity_by_tag('player'), MOVEMENT_KEYS[key]))
        #self._terminal.puts(10,10, '[color=orange]{}[/color]'.format(key))
