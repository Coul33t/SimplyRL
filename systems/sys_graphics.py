from components.graphics import Graphics

class SysGraphics:
    def __init__(self):
        self.component_list = {}

    def create_component(self, entity, **params):
        self.component_list[entity] = Graphics(**params)

    def update(self):
        pass
