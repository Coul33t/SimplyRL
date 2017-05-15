import uuid
import pdb

from collections import OrderedDict

class EntityManager:
    def __init__(self):
        self._entities_list = []
        self._entities_tag = OrderedDict()
        self._systems_dict = OrderedDict()

    def create_entity(self):
        self._entities_list.append(uuid.uuid4())
        return self._entities_list[-1]

    def subscribe_system(self, system, name):
        self._systems_dict[name] = system
        system.set_ref_to_entity_manager(self)

    def get_system(self, system):
        if system in self._systems_dict:
            return self._systems_dict[system]
        return None

    def add_component(self, entity, component, **params):
        if entity not in self._entities_list:
            return False

        if component not in self._systems_dict:
            return False

        sys = self._systems_dict[component]
        return sys.create_component(entity, **params)

    def associate_tag(self, entity, tag):
        if tag in self._entities_tag:
            self._entities_tag[tag].append(entity)

        else:
            self._entities_tag[tag] = entity

    def dissociate_tag(self, entity, tag):
        if tag in self._entities_tag and entity in self._entities_tag[tag]:
            self._entities_tag[tag].remove(entity)

    def get_entity_by_tag(self, tag):
        return self._entities_tag[tag]

    def update(self):
        for sys in self._systems_dict:
            self._systems_dict[sys].update()
