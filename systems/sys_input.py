from systems.sys_template import *

MOVEMENT_KEYS = {93: [0, 0], 90: [0, 1], 89: [-1, 1], 92: [-1, 0], 95: [-1, -1], 96: [0, -1], 97: [1, -1],
                 94: [1, 0], 91: [1, 1]}

QUIT_KEY = (41, 224)

class SysInput(SysTemplate):
    def __init__(self, terminal=None, engine=None):
        super().__init__()
        self._terminal = terminal
        self._engine = engine

    def update(self):
        key = self._terminal.read()

        if key in QUIT_KEY:
            self._engine.game_state = 'exit'

        if key in MOVEMENT_KEYS:
            self.entity_manager.get_system('Event').add_event(('Physics', 'move', self.entity_manager.get_entity_by_tag('Player'), MOVEMENT_KEYS[key]))
        #self._terminal.puts(10,10, '[color=orange]{}[/color]'.format(key))
