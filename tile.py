class Tile:
    def __init__(self, ch, blocked=True, block_sight=True, fg='255,255,255', bg=None):
        self._ch = ch
        self._explored = False
        self._blocked = blocked
        self._block_sight = block_sight
        self._fg = fg
        self._bg = bg

    def _get_ch(self):
        return self._ch

    def _set_ch(self, ch):
        self._ch = ch

    ch = property(_get_ch, _set_ch)

    def _get_explored(self):
        return self._explored

    def _set_explored(self, explored):
        self._explored = explored

    explored = property(_get_explored, _set_explored)

    def _get_blocked(self):
        return self._blocked

    def _set_blocked(self, blocked):
        self._blocked = blocked

    blocked = property(_get_blocked, _set_blocked)

    def _get_block_sight(self):
        return self._block_sight

    def _set_block_sight(self, block_sight):
        self._block_sight = block_sight

    block_sight = property(_get_block_sight, _set_block_sight)

    def _get_fg(self):
        return self._fg

    def _set_fg(self, fg):
        self._fg = fg

    fg = property(_get_fg, _set_fg)

    def _get_bg(self):
        return self._bg

    def _set_bg(self, bg):
        self._bg = bg

    bg = property(_get_bg, _set_bg)