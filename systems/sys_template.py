from collections import OrderedDict
import pdb

class SysTemplate:
    def __init__(self):
        # A dictionnary of components
        self.component_list = OrderedDict()
        # Reference to the entity manager
        self.entity_manager = None

    def create_component(self, entity, **params):
        pass
        #print('Component creation not implemented for the current system ({}).'.format(self.__class__.__name__))

    def delete_component(self, comp_id):
        if comp_id in self.component_list:
            del self.component_list[comp_id]

    def get_component(self, comp_id):
        if comp_id in self.component_list:
            return self.component_list[comp_id]

    def set_ref_to_entity_manager(self, manager):
        self.entity_manager = manager

    def update(self):
        pass
        #print('Update function not implemented for the current system ({}).'.format(self.__class__.__name__))
