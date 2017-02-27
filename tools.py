import random as rn

# Return a random color, based on an initial color
def rnd_color(base, factor, same=False):
    base = base.split(',')
    base = [int(x) for x in base]

    if(same):
        f = rn.randint(0 - round(base[0]*factor[0]/2), round(base[0]*factor[0]/2))
        r = base[0] + f
        g = base[1] + f
        b = base[2] + f
    else:
        r = base[0] + rn.randint(0 - round(base[0]*factor[0]/2), round(base[0]*factor[0]/2))
        g = base[1] + rn.randint(0 - round(base[1]*factor[1]/2), round(base[1]*factor[1]/2))
        b = base[2] + rn.randint(0 - round(base[2]*factor[2]/2), round(base[2]*factor[2]/2))
    
    if r > 255:
        r = 255
    if r < 0:
        r = 0

    if g > 255:
        g = 255
    if g < 0:
        g = 0

    if b > 255:
        b = 255
    if b < 0:
        b = 0

    return str(r) + ',' + str(g) + ',' + str(b)


# Rectangle class (useful for rooms)
class Rect:
    def __init__(self, x, y, w, h):
        self._x1 = x
        self._y1 = y
        self._x2 = x + w
        self._y2 = y + h

    def _get_x1(self):
        return self._x1

    def _set_x1(self, x1):
        self._x1 = x1

    x1 = property(_get_x1, _set_x1)

    def _get_y1(self):
        return self._y1

    def _set_y1(self, y1):
        self._y1 = y1

    y1 = property(_get_y1, _set_y1)

    def _get_x2(self):
        return self._x2

    def _set_x2(self, x2):
        self._x2 = x2

    x2 = property(_get_x2, _set_x2)

    def _get_y2(self):
        return self._y2

    def _set_y2(self, y2):
        self._y2 = y2

    y2 = property(_get_y2, _set_y2)

    def get_center(self):
        return ((int)((self._x1 + self._x2)/2), (int)((self._y1 + self._y2)/2))

    def intersect(self, other_rect):
        return (self._x1 <= other_rect.x2 and self._x2 >= other_rect.x1 and
                self._y1 <= other_rect.y2 and self._y2 >= other_rect.y1)