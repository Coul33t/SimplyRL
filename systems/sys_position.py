from components.position import Position

class SysPosition:
    def __init__(self):
        self._component_list = {}

    def create_component(self, entity, **params):
        self._component_list[entity] = Position(**params)

    def update(self):
        pass
