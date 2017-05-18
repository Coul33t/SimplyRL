from components.physics import Physics
from systems.sys_template import *

class SysPhysics(SysTemplate):
    def __init__(self):
        super().__init__()

    def create_component(self, entity, **params):
        self.component_list[entity] = Physics(**params)

    def move(self, entity, delta):
        if entity in self.component_list:
            if not self.entity_manager.get_system('Map').is_blocked(
                self.component_list[entity].x + delta[0],
                self.component_list[entity].y + delta[1]):

                self.component_list[entity].x += delta[0]
                self.component_list[entity].y += delta[1]
