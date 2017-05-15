from systems.sys_template import *

class SysEvent(SysTemplate):
    def __init__(self):
        self._event_queue = []
        self._entity_manager = None

    # An event is : a system, a function, a value
    def add_event(self, event):
        if len(event) == 3:
            self._event_queue.append(event)

    def update(self):
        manager = self._entity_manager

        for event in self._event_queue:
            print(event)
            getattr(manager.get_system(event[0]), event[1])(event[2])

        self._event_queue = []
