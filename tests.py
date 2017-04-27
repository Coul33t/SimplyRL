from entities.entities_manager import EntityManager
from systems.sys_position import SysPosition
from systems.sys_graphics import SysGraphics


entity_manager = EntityManager()
sys1 = SysPosition()
sys2 = SysGraphics()

entity_manager.subscribe_system(sys1, 'position')
entity_manager.subscribe_system(sys2, 'graphics')

entity_manager.update()
