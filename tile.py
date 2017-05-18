class Tile:
    def __init__(self, ch, blocked=True, block_sight=True, fg='255,255,255', bg=None):
        self.ch = ch
        self.explored = False
        self.blocked = blocked
        self.block_sight = block_sight
        self.fg = fg
        self.bg = bg
