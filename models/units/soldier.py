from random import randint
from time import monotonic
from .unit import Unit


@Unit.register('Soldier')
class Soldier(Unit):

    def __init__(self, health=100):
        self.recharge = randint(100, 2000)
        self.health = health
        self.zero_time = 0
        self.exp = 0

    def recharger(self):
        if (self.zero_time + self.recharge) <= monotonic() * 1000:
            return True
        else:
            return False

    def level_up(self):
        if self.exp != 50:
            self.exp += 1
            return self.exp
        else:
            return self.exp

    def is_attack(self):
        calc_chance = 0.5 * (1 + self.health / 100) * \
            randint((50 + self.exp), 100) / 100
        return calc_chance

    def demage(self):
        if self.recharger() == True:
            calc_demage = 0.05 + self.exp / 100
            self.zero_time = monotonic() * 1000
            self.level_up()
            return calc_demage
        else:
            return 0

    def demage_rank(self):
        demage_calc = 0.05 + self.exp / 100
        return demage_calc

    def take_damage(self, demag_enemy):
        if self.is_active() == True:
            self.health -= demag_enemy
        return self.health

    def is_active(self):
        if self.health <= 0:
            return False
        else:
            return True

    def __str__(self):
        return 'Soldier: recharge:{0} health:{1}'.format(self.recharge, self. health)
