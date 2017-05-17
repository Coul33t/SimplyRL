from components.position import Position
from systems.sys_template import *

class SysPosition(SysTemplate):
    def __init__(self):
        super().__init__()

    def create_component(self, entity, **params):
        self._component_list[entity] = Position(**params)

    def move(self, entity, delta):
        if entity in self._component_list:
            self._component_list[entity].x += delta[0]
            self._component_list[entity].y += delta[1]
