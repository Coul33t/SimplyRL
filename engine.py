from bearlibterminal import terminal
import tdl

import pdb

from entities.entities_manager import *
from tags_manager import *

from systems.sys_input import *
from systems.sys_physics import *
from systems.sys_map import *
from systems.sys_event import *
from systems.sys_render import *

class Engine:
    def __init__(self):
        self.game_state = 'main_menu'

        self.init_terminal()

        self._entities_manager = EntityManager()

        self._entities_manager.subscribe_system(SysInput(terminal, self), 'Input')
        self._entities_manager.subscribe_system(SysPhysics(), 'Physics')
        self._entities_manager.subscribe_system(SysEvent(), 'Event')
        self._entities_manager.subscribe_system(SysMap(), 'Map')
        self._entities_manager.subscribe_system(SysRender(terminal), 'Graphics')

        (x_player, y_player) = self._entities_manager.get_system('Map').game_map.create_map()

        self._player = self._entities_manager.create_entity()

        self._entities_manager.add_component(self._player, 'Physics', x=x_player, y=y_player, blocks_sight=False)
        self._entities_manager.add_component(self._player, 'Graphics', ch='@', fg='red', bg=None)

        self._entities_manager.associate_tag(self._player, 'player')

        self.game_state = 'playing'


    def init_terminal(self):
        terminal.open()
        terminal.set("window.size=64x20, font: res/fonts/VeraMono.ttf, size=10x20")
        terminal.set("window.title='SimplyRL'")
        terminal.set("font: res/fonts/VeraMono.ttf, size=20x40")
        terminal.composition(True)
        terminal.refresh()


    def send_to_back(self, entity):
        self._entities.remove(entity)
        self._entities.insert(0, entity)


    def update(self):
        for sys in self._entities_manager._systems_dict:
            #print("{} system called".format(sys))
            self._entities_manager._systems_dict[sys].update()
