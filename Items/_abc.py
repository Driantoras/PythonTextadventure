from utilities import *


class Item:
    name = ''
    description = ''
    type = None
    stackable = None
    value = 0
    lvl_req = 1

    attack_damage = None
    attack_speed = None
    crit_rate = None
    crit_multiplier = None
    armor = None
    effect = None
    crafting = None

    def __repr__(self):
        print_str = [f'{BOLD}{self.name}{NORMAL}',
                     f'{ITALIC}{self.description}{NORMAL}',
                     f'- Wert: {YELLOW}{self.value}🪙{NORMAL}']

        if self.type == 'weapon':
            print_str += [f'- Schaden: {self.attack_damage}',
                          f'- Krit. Chance: {self.crit_rate:2.2%}',
                          f'- Krit. Multiplikator: {self.crit_multiplier}']

        elif self.type == 'armor':
            print_str += [f'- Rüstungspunkte: {self.armor}']

        elif self.type == 'consumable':
            print_str += [f'- Effekt: {self.effect["hp"]:+} Lebenspunkte']

        return '\n'.join(print_str) + '\n'


class Ressource(Item):
    type = 'ressource'
    stackable = True


class Consumable(Item):
    type = 'consumable'
    stackable = True

    effect = {}


class Weapon(Item):
    type = 'weapon'
    stackable = False

    attack_damage = 1
    attack_speed = 1
    crit_rate = 0.05
    crit_multiplier = 1.5


class Armor(Item):
    type = 'armor'
    stackable = False

    armor = 0
