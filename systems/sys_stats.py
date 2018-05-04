from components.stats import Stats
from systems.sys_template import *
import pdb

class SysStats(SysTemplate):
    def __init__(self):
        super().__init__()
        
    def create_component(self, entity, **params):
        self.component_list[entity] = Stats(**params)
    
    def update(self):
        to_delete = []
        
        for elem in self.component_list:
            e = self.entity_manager.get_system('Stats').get_component(elem)
            if e.hp <= 0:
                # Can't mutate dict during iteration over it
                to_delete.append(elem)

        for elem in to_delete:
            self.entity_manager.delete_entity(elem)