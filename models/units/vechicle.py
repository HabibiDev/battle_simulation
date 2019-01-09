from random import randint
from time import time
from .unit import Unit
from .soldier import Soldier


@Unit.register('Vehicle')
class Vehicle(Unit):

    def __init__(self, health=100):
        self.operators = [Soldier() for i in range(randint(1, 4))]
        self.recharge = randint(1000, 2000)
        self.health = health
        self.zero_time = 0
        self.exp = 0
        self.rank_vehicle = 0

    def recharger(self):
        if (self.zero_time + self.recharge) <= time() * 1000:
            return True
        else:
            return False

    def is_active(self):
        if self.health > 0 and len(self.operators) != 0:
            return True
        else:
            return False

    def take_damage(self, demag_enemy):
        self.health -= 0.6 * demag_enemy
        calc_operators = len(self.operators)
        number_of_operators = randint(0, calc_operators - 1)

        if len(self.operators) != 0:
            for i in range(len(self.operators)):
                if i != number_of_operators:
                    if self.operators[i].is_active() == True:
                        self.operators[i].take_damage(0.1 * demag_enemy)
                    else:
                        del self.operators[i]

        if self.operators[number_of_operators].is_active() == True:
            self.operators[number_of_operators].take_damage(0.2 * demag_enemy)
        else:
            del self.operators[number_of_operators]
        return self.health

    def level_up(self):
        for oper in self.operators:
            oper.level_up()

    def is_attack(self):
        gavg = 1
        for attack in self.operators:
            gavg *= attack.is_attack()
        gavg = gavg ** (1 / len(self.operators))
        calc_chance = 0.5 * (1 + self.health / 100) * gavg
        return calc_chance

    def demage(self):
        if self.recharger() == True:
            operators_exp = [i.exp for i in self.operators]
            calc_demage = 0.05 + sum(operators_exp) / 100
            self.zero_time = time() * 1000
            self.level_up()
            return calc_demage
        else:
            return 0

    def demage_rank(self):
        operators_exp = [i.exp for i in self.operators]
        demage_calc = 0.05 + sum(operators_exp) / 100
        return demage_calc

    def __str__(self):
        return 'Vehicle: recharge:{0} health:{1}\n operators:{2}'.format(self.recharge, self.health, self.operators)
