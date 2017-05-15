from collections import OrderedDict

class TagManager:
    def __init__(self):
        self._entities_tag = OrderedDict()

    def associate_tag(self, entity, tag):
        if entity in self._entities_tag:
            self._entities_tag[entity].append(tag)

        else:
            self._entities_tag[entity] = [tag]

    def dissociate_tag(self, entity, tag):
        if entity in self._entities_tag and tag in self._entities_tag[entity]:
            self._entities_tag[entity].remove(tag)
