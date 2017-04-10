from ecs.component import *

class Graphics(Component):
    def __init__(self, ch='X', fg=None, bg=None):
        super().__init__('GRAPHICS')
        self.ch = ch
        self.fg = fg
        self.bg = bg