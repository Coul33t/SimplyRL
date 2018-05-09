from components.message import Message
from systems.sys_template import *

ENTITIY_DEFAULT_FG_COLOUR = {}
ENTITIY_DEFAULT_BG_COLOUR = {}

class SysMessages(SysTemplate):
    def __init__(self):
        super().__init__()
        self._message_history = []

    def create_component(self, entity, **params):
        if 'fg_colour' in params and params['fg_colour'] == 'default':
            #params['fg_colour'] = ENTITIY_DEFAULT_FG_COLOURS[entity]
            params['fg_colour'] = '255,255,255'
        if 'bg_colour' in params and params['bg_colour'] == 'default':
            #params['bg_colour'] = ENTITIY_DEFAULT_BG_COLOURS[entity]
            params['bg_colour'] = '0,0,0'

        self.component_list[entity] = Message(**params)
        self._message_history.append(Message(**params))

    def return_msg(self, number=0):
        if number > len(self._message_history):
            number = len(self._message_history)
        return self._message_history[(len(self._message_history) - number):][::-1]

