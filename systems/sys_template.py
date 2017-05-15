from collections import OrderedDict

class SysTemplate:
    def __init__(self):
        # A dictionnary of components
        self._component_list = OrderedDict()
        # Reference to the entity manager
        self._entity_manager = None

    def create_component(self, entity, **params):
        print('Component creation not implemented for the current system ({}).'.format(self.__class__.__name__))

    def get_component(self, comp_id):
        if comp_id in self._component_list:
            return self._component_list[comp_id]

    def set_ref_to_entity_manager(self, manager):
        self._entity_manager = manager

    def update(self):
        print('Update function not implemented for the current system ({}).'.format(self.__class__.__name__))
