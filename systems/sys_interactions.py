from components.interactions import Interactions
from systems.sys_template import *

class SysInteractions(SysTemplate):
    def __init__(self):
        super().__init__()
        
    def create_component(self, entity, **params):
        self.component_list[entity] = Interactions(**params)
        
    def melee_attack(self, entity, target):
        e = self.entity_manager.get_system('Stats').get_component(entity)
        t = self.entity_manager.get_system('Stats').get_component(target)
        
        t.hp -= e.melee_dmg