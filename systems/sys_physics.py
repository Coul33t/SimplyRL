from components.physics import Physics
from systems.sys_template import *

class SysPhysics(SysTemplate):
    def __init__(self):
        super().__init__()

    def create_component(self, entity, **params):
        self.component_list[entity] = Physics(**params)

    def distance_to(self, other):
        return round(math.sqrt((other.x - self._x)**2 + (other.y - self._y)**2))

    def get_entity_from_coordinates(self, x, y):
        for entity in self.component_list:
            e = self.entity_manager.get_system('Physics').get_component(entity)
            if e.x == x and e.y == y:
                return entity
        return None

    def move(self, entity, delta):
        if entity not in self.component_list:
            return

        new_x = self.component_list[entity].x + delta[0]
        new_y = self.component_list[entity].y + delta[1]

        # There is nothing blocking the path
        if not self.entity_manager.get_system('Map').is_blocked(new_x, new_y):
            self.component_list[entity].x = new_x
            self.component_list[entity].y = new_y

        # There is something blocking the path
        else:
            # If it's an actual entity
            target = self.get_entity_from_coordinates(new_x, new_y)

            if target is None:
                return

            # If the target can be interacted with and has stats and can be attacked
            if self.entity_manager.get_system('Interactions').get_component(target) and\
               self.entity_manager.get_system('Stats').get_component(target) and\
               'attack' in self.entity_manager.get_system('Interactions').get_component(target).can_be_interacted:

                e_name = self.entity_manager.get_system('Graphics').get_component(entity).name
                t_name = self.entity_manager.get_system('Graphics').get_component(target).name
                msg = f'{e_name} attacks {t_name}'
                if e_name == 'You':
                    msg = f'{e_name} attack the {t_name}'
                # We attack it
                self.entity_manager.get_system('Interactions').melee_attack(entity, target)
                self.entity_manager.add_component(entity, 'Messages', txt=msg, fg_colour='255,150,150', bg_colour='0,0,0')













