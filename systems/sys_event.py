from systems.sys_template import *
import pdb

class SysEvent(SysTemplate):
    def __init__(self):
        super().__init__()
        self._event_queue = []

    # An event is : a system, a function, an entity, a value
    def add_event(self, event):
        if len(event) == 4:
            self._event_queue.append(event)
        else:
            print('Wrong number of event values (should be : [0] a system [1] a function [2] an entity [3] a value)')

    def update(self):
        manager = self.entity_manager

        for event in self._event_queue:
            getattr(manager.get_system(event[0]), event[1])(event[2], event[3])

        self._event_queue = []
