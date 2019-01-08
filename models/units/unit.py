import random
from time import time

class Unit:
	def __init__(self, health = 100):
		self.recharge = random.randint(100, 2000)
		self.health = health
		self.zero_time = 0


	def recharger(self):
		if (self.zero_time + self.recharge) <= time() * 1000:
			return True
		else:
			return False