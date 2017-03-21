class Entity:
    def __init__(self):
        self._component_list = []

    def _get_component_list(self):
        return self._component_list

    def _set_component_list(self):
        pass

    component_list = property(_get_component_list, _set_component_list)

    def _add_component(self, comp):
        self._component_list.append(comp)
