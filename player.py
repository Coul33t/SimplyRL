from ecs.entity import *
from components.position import *
from components.graphics import *

class Player(Entity):
    def __init__(self, x=0, y=0, ch='@', fg='white', bg=None):
        super().__init__('player')
        self.add_component(Position(x, y))
        self.add_component(Graphics(ch, fg, bg))
