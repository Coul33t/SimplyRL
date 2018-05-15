from tools import distance

class Ai(object):
    def __init__(self, ai_type='basic'):
        self.ai_type = ai_type
        self.last_seen_player = (None, None)