from components.ai import Ai
from systems.sys_template import *

class SysAi(SysTemplate):
    def __init__(self):
        super().__init__()

    def create_component(self, entity, **params):
        self.component_list[entity] = Ai(**params)

    def basic(self):
        pass

    def update(self):
        pass

