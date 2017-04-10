class System:
    def __init__(self):
        self._components_tagged = []

    def _get_components_tagged(self):
        return self._components_tagged

    def _set_components_tagged(self):
        pass

    components_tagged = property(_get_components_tagged, _set_components_tagged)

    def add_component_tag(self, tag):
        if tag.upper() not in self._components_tagged:
            self._components_tagged.append(tag.upper())
            return True
            
        return False

    def del_component_tag(self, tag):
        if tag.upper() in self._components_tagged:
            self._components_tagged.remove(tag)
            return True

        return False 

    def _init(self):
        pass

    def update(self):
        pass
