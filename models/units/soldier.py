import random
from time import time
from .unit import Unit

class Soldier(Unit):

	def __init__(self):
		Unit.__init__(self, health = 100)
		self.exp = 0
		

	def level_up(self):
		if self.exp != 50:
			self.exp += 1
			return self.exp
		else:
			return self.exp

	def is_attack(self):
		calc_chance = 0.5 * (1 + self.health / 100) * random.randint((50 + self.exp), 100) / 100
		return calc_chance

	def demage(self):
		if self.recharger() == True:
			calc_demage = 0.5 + self.exp/100
			self.zero_time = time() * 1000
			self.level_up()
			return calc_demage
		else:
			return 0
	
	def demage_rank(self):
		demage_calc = 0.5 + self.exp/100
		return demage_calc


	def take_damage(self, demag_enemy):
		if self.is_active() == True:
			self.health -= demag_enemy
		return self.health

	def is_active(self):
		if self.health<=0:
			return False
		else:
			return True

	def __str__(self):
		return 'Soldier: recharge:{0} health:{1}'.format(self.recharge, self. health)