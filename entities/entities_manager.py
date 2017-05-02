import uuid
import pdb

class EntityManager:
    def __init__(self):
        self._entities_list = []
        self._systems_dict = {}

    def create_entity(self):
        self._entities_list.append(uuid.uuid4())
        return self._entities_list[-1]

    def subscribe_system(self, system, name):
        self._systems_dict[name] = system

    def add_component(self, entity, component, **params):
        if entity not in self._entities_list:
            return False

        if component not in self._systems_dict:
            return False

        sys = self._systems_dict[component]
        return sys.create_component(entity, **params)

    def update(self):
        for sys in self._systems_dict:
            self._systems_dict[sys].update()
