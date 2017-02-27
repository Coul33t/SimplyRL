class Tile:
    def __init__(self, ch, blocked=True, block_sight=True, fgd_color='255,255,255', bkg_color=None):
        self._ch = ch
        self._explored = False
        self._blocked = blocked
        self._block_sight = block_sight
        self._fgd_color = fgd_color
        self._bkg_color = bkg_color

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

    def _get_fgd_color(self):
        return self._fgd_color

    def _set_fgd_color(self, fgd_color):
        self._fgd_color = fgd_color

    fgd_color = property(_get_fgd_color, _set_fgd_color)

    def _get_bkg_color(self):
        return self._bkg_color

    def _set_bkg_color(self, bkg_color):
        self._bkg_color = bkg_color

    bkg_color = property(_get_bkg_color, _set_bkg_color)