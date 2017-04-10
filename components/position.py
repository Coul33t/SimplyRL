from ecs.component import *

class Position(Component):
    def __init__(self, x=0, y=0):
        super().__init__('POSITION')
        self.x = x
        self.y = y