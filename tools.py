import random as rn

def distance(p1,p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 ) ** 0.5

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
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def get_center(self):
        return ((int)((self.x1 + self.x2)/2), (int)((self.y1 + self.y2)/2))

    def intersect(self, other_rect):
        return (self.x1 <= other_rect.x2 and self.x2 >= other_rect.x1 and
                self.y1 <= other_rect.y2 and self.y2 >= other_rect.y1)
