class Squad:

    def __init__(self, units):
        self.units = units
        self.rank = 0

    def is_active(self):
        squad_active = False
        for unit in self.units:
            if unit.is_active() == True:
                squad_active = True
            else:
                self.units.remove(unit)
        return squad_active

    def is_attack(self):
        gavg = 1
        for unit in self.units:
            gavg *= unit.is_attack()
        gavg = gavg ** (1 / len(self.units))
        calc_chance = 0.5 * (1 + unit.health / 100) * gavg
        return calc_chance

    def demage(self):
        calc_demage = 0
        for unit in self.units:
            calc_demage += unit.demage()
        return calc_demage

    def take_damage(self, demag_squad):
        for unit in self.units:
            unit.take_damage(demag_squad / len(self.units))

    def squad_rank(self):
        power_level = 0
        for unit in self.units:
            power_level += unit.demage_rank()
        return power_level

    def __str__(self):
        return 'Squad:\n Units:{0}\n'.format(self.units)
