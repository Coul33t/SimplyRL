from components.graphics import Graphics

class SysGraphics:
    def __init__(self):
        self._component_list = {}

    def create_component(self, entity, **params):
        self._component_list[entity] = Graphics(**params)

    def update(self):
        pass
