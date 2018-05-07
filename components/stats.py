class Stats(object):
	def __init__(self, hp=1, stamina=0, mana=0, defense=0,
				 melee_dmg=0, ranged_dmg=0, level=1, xp=0,
				 xp_given=0, is_dead=False, vision_range=5):

		self.hp = hp
		self.stamina = stamina
		self.mana = mana
		self.defense = defense
		self.melee_dmg = melee_dmg
		self.ranged_dmg = ranged_dmg
		self.level = level
		self.xp = xp
		self.xp_given = xp_given
		self.is_dead = is_dead
		self.vision_range = vision_range
