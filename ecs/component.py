class Component:
    def __init__(self, name='DEFAULT'):
        self._name = name

    def _get_name(self):
        return self._name

    def _set_name(self):
        pass

    name = property(_get_name, _set_name)
