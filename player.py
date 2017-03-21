from ecs.entity import *

class Player(Entity):
    def __init__(self, x, y, ch='@', bg=None, fg='white'):
        self._x = x
        self._y = y
        self._ch = ch
        self._bg = bg
        self._fg = fg


    def _get_x(self):
        return self._x

    def _set_x(self, x):
        self._x = x

    x = property(_get_x, _set_x)

    def _get_y(self):
        return self._y

    def _set_y(self, y):
        self._y = y

    y = property(_get_y, _set_y)

    def _get_ch(self):
        return self._ch

    def _set_ch(self, ch):
        self._ch = ch

    ch = property(_get_ch, _set_ch)

    def _get_bg(self):
        return self._bg

    def _set_bg(self, bg):
        self._bg = bg

    bg = property(_get_bg, _set_bg)

    def _get_fg(self):
        return self._fg

    def _set_fg(self, fg):
        self._fg = fg

    fg = property(_get_fg, _set_fg)