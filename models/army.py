import random
from .units.soldier import Soldier
from .units.vechicle import Vehicle
from models.squad import Squad


class Army:

    def __init__(self, squads, number):
        self.armies = []
        self.squads = squads
        self.squads_list = []
        self.choose_army = None
        self.number = number
        self.rank = 0

    def create_army(self):
        for squad in range(self.squads):
            units = random.randint(5, 11)
            unit_soldier = random.randint(1, units - 1)
            units_list = []
            for unit in range(unit_soldier):
                units_list.append(Soldier())
            for unit_vehicle in range(units - unit_soldier):
                units_list.append(Vehicle())
            self.squads_list.append(Squad(units_list))
        return self.squads_list

    def is_attack(self):
        calc_chance = 0
        for squad in self.squads_list:
            calc_chance += squad.is_attack()
        return calc_chance

    def is_active(self):
        army_active = False
        for squad in self.squads_list:
            if squad.is_active() == True:
                army_active = True
            else:
                self.squads_list.remove(squad)
        return army_active

    def demage(self):
        demage_calc = 0
        for squad in self.squads_list:
            demage_calc += squad.demage()
        return demage_calc

    def choose_strategy(self):
        my_strategy = random.choice(['random', 'weakest', 'strongest'])
        if my_strategy == 'random':
            self.choose_army = random.choice(self.armies)
        elif my_strategy == 'weakest':
            rank = random.choice(self.armies).rank_army()
            for army in self.armies:
                if rank > army.rank_army():
                    rank = army.rank_army()
                    self.choose_army = army
                else:
                    self.choose_army = army
        elif my_strategy == 'strongest':
            rank = random.choice(self.armies).rank_army()
            for army in self.armies:
                if rank < army.rank_army():
                    rank = army.rank_army()
                    self.choose_army = army
                else:
                    self.choose_army = army
        return self.choose_army

    def take_damage(self, army_demage):
        for squad in self.squads_list:
            squad.take_damage(army_demage / len(self.squads_list))

    def attack_success(self, army_attack, demage):
        if self.is_attack() < army_attack.is_attack():
            self.take_damage(demage)

    def rank_army(self):
        for squad in self.squads_list:
            self.rank += squad.squad_rank()
        return self.rank

    def __str__(self):
        return 'Army_{0}'.format(self.number)
