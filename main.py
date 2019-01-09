from random import randint
from models.army import Army
from battle import Battle

if __name__ == '__main__':

    armies = []
    try:
        calc_army = int(
            input('Enter how many armies are playing (min = 2): \n')
        )

        if calc_army < 2:
            print('You entered less then 2 armies')
        else:
            for i in range(calc_army):
                calc_squad = int(
                    input(
                        'Enter how many squads for Army_{0} (min = 1):\n'.format(i))
                )
                army = Army(randint(2, calc_squad), i)
                army.create_army()
                army.rank_army()
                armies.append(army)

            Game = Battle(armies)
            Game.battle_armies()
            print(Game)
    except ValueError:
        print('Wrong input, you must input only number')
