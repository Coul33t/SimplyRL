from entity import *
from component import *
from system import *

import unittest

class ECSTest(unittest.TestCase):

    def test_entity_mutators(self):
        ent = Entity()
        # Check for the name
        self.assertEqual(ent.guid, 'DEFAULT')
        # Check for the list
        self.assertEqual(ent.component_list, {})

    def test_entity_add_comp(self):
        ent = Entity()
        comp = Component()

        # Check return value when adding a comp
        self.assertTrue(ent.add_component(comp))
        # Check if you can't add the same comp twice
        self.assertFalse(ent.add_component(comp))

    def test_entity_del_comp(self):
        ent = Entity()
        comp = Component()

        ent.add_component(comp)

        # Check comp deleting 
        self.assertTrue(ent.del_component(comp.name))
        # Check if you can't delete an unexisting comp
        self.assertFalse(ent.del_component(comp.name))

    def test_entity_has_comp(self):
        ent = Entity()
        comp = Component()

        # Check if has a comp
        self.assertFalse(ent.has_comp(comp.name))

        ent.add_component(comp)

        # Check if the ent have the comp
        self.assertTrue(ent.has_comp(comp.name))

        
    def test_component_mutators(self):
        comp = Component()

        self.assertEqual(comp.name, 'DEFAULT')

    def test_component_add_comp_tag(self):
        sys = System()

        # Check if you can add a tag
        self.assertTrue(sys.add_component_tag('TEST'))
        # Check if you can't add the same tag twice
        self.assertFalse(sys.add_component_tag('TEST'))

    def test_component_del_comp_tag(self):
        sys = System()
        sys.add_component_tag('TEST')

        # Check if you can add a tag
        self.assertTrue(sys.del_component_tag('TEST'))
        # Check if you can't add the same tag twice
        self.assertFalse(sys.del_component_tag('TEST'))


if __name__ == '__main__':
    unittest.main()