class Graphics(object):
    def __init__(self, ch='X', name='NONE', fg=None, bg=None, always_visible=False):
        self.ch = ch
        self.name = name
        self.fg = fg
        self.bg = bg
        self.always_visible = always_visible
        self.last_seen = [None, None]
