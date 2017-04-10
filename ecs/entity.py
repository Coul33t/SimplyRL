class Entity:
    def __init__(self, guid = 'DEFAULT'):
        self._guid = guid
        self._component_list = {}

    def _get_component_list(self):
        return self._component_list

    def _set_component_list(self):
        pass

    component_list = property(_get_component_list, _set_component_list)

    def _get_guid(self):
        return self._guid

    def _set_guid(self):
        pass

    guid = property(_get_guid, _set_guid)


    def add_component(self, comp):
        if comp.name.upper() not in self._component_list:
            self._component_list[comp.name] = comp
            return True

        return False


    def del_component(self, name):
        if name.upper() in self._component_list:
            del self._component_list[name]
            return True

        return False


    def has_comp(self, name):
        return name.upper() in self._component_list
