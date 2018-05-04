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
        if entity in self.component_list:

            new_x = self.component_list[entity].x + delta[0]
            new_y = self.component_list[entity].y + delta[1]

            # There is nothing blocking the path
            if not self.entity_manager.get_system('Map').is_blocked(new_x, new_y):
                self.component_list[entity].x = new_x
                self.component_list[entity].y = new_y
                self.entity_manager.add_component(entity, 'Messages',txt='Move')

            # There is something blocking the path
            else:
                # If it's an actual entity
                target = self.get_entity_from_coordinates(new_x, new_y)

                if target is not None:
                    # If the target can be interacted with
                    if self.entity_manager.get_system('Interactions').get_component(target):

                        # If the target has stats
                        if self.entity_manager.get_system('Stats').get_component(target):

                            # If it can be attacked
                            if 'attack' in self.entity_manager.get_system('Interactions').get_component(target).can_be_interacted:
                                # We attack it
                                self.entity_manager.get_system('Interactions').melee_attack(entity, target)
                                self.entity_manager.add_component(entity, 'Messages',txt='Attack')













