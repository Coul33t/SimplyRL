class Component:
    def __init__(self, name='default', tags='default'):
        self._name = name
        self._tags = tags

    def _get_name(self):
        return self._name

    def _set_name(self):
        pass

    name = property(_get_name, _set_name)

    def _get_tags(self):
        return self._tags

    def _set_tags(self, tags):
        pass

    tags = property(_get_tags, _set_tags)

    def _add_tag(self, tag):
        self._tags.append(tag)
