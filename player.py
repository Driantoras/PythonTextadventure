import math
import random

import Items
from utilities import *
from inventory import Inventory


class Player:
    def __init__(self):
        self.level = 1
        self._exp = 0
        self.exp_max = 100

        self.hp_max = 100
        self._hp = self.hp_max

        self.base_dmg = self.level - 1

        self.gold = 0
        self.inventory = Inventory()
        self.hand = None
        self.body = None

        self.alive = True

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value > self.hp_max:
            self._hp = self.hp_max
        elif value <= 0:
            print(f'{RED}{BOLD}Du bist gestorben{NORMAL}')
            self.alive = False
        else:
            self._hp = value

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value
        while self.exp >= self.exp_max:
            print(f'Level: {BOLD}{self.level}{NORMAL} -> {GREEN}{BOLD}{self.level + 1}{NORMAL}')
            self._exp -= self.exp_max
            self.level += 1
            self.exp_max = int(round(100 * (1.2 ** (self.level - 1)), -1))
            self.hp_max = 100 + (5 * (self.level - 1))
            self._hp = self.hp_max

    def receive_exp(self, ep: int):
        print(f'{ADDED} {CYAN}{ep}EP{NORMAL}')
        self.exp += ep

    def add_gold(self, amount):
        if amount is not None:
            if type(amount) is tuple:
                amount = random.randint(*amount)
            self.gold += amount
            print(f'{ADDED} {YELLOW}{amount}🪙{NORMAL}')

    def print_gold(self):
        print(f'{YELLOW}{self.gold}🪙{NORMAL}')

    def print_stats(self):
        print(
            f'Level: {self.level}\n'
            f'Erfahrungspunkte: {self.exp} von {self.exp_max}\n'
            f'Lebenspunkte: {self.hp} von {self.hp_max}\n')

    def print_gear(self):
        if self.hand is not None:
            print(
                f'{BOLD}{UNDERLINED}{self.hand.name}{NORMAL}\n'
                f'- Schaden: {self.hand.attack_damage}\n'
                f'- Krit. Chance: {self.hand.crit_rate:2.2%}\n'
                f'- Krit. Multiplikator: {self.hand.crit_multiplier}\n')
        else:
            print(f'\nkeine Waffe ausgerüstet')

        if self.body is not None:
            print(
                f'{BOLD}{UNDERLINED}{self.body.name}{NORMAL}\n'
                f'- Rüstungspunkte: {self.body.armor}')
        else:
            print(f'keine Rüstung ausgerüstet')

    def attack_enemy(self, enemy):
        is_crit = False
        no_weapon = self.hand is None
        deal_dmg = self.base_dmg

        if no_weapon:
            deal_dmg += 3
        else:
            deal_dmg += self.hand.attack_damage
            if random.random() <= self.hand.crit_rate:
                deal_dmg = int(deal_dmg * self.hand.crit_multiplier)
                is_crit = True

        enemy.hp -= deal_dmg
        print(f'Du hast {RED if is_crit else ""}{BOLD}{deal_dmg}{NORMAL} Schaden '
              f'{"mit deinen Fäusten " if no_weapon else ""}verursacht.')

    def get_attacked(self, enemy):
        is_crit = False
        take_dmg = enemy.attack_damage
        if random.random() <= enemy.crit_rate:
            take_dmg = int(take_dmg * enemy.crit_multiplier)
            is_crit = True
        if self.body is not None:
            take_dmg = int(round(take_dmg / (1 + (math.sqrt(self.body.armor * 20) / 100)), 0))

        self.hp -= take_dmg
        print(f'Der Gegner hat dir {RED if is_crit else ""}{BOLD}{take_dmg}{NORMAL} Schaden zugefügt.')

    def use_item(self, item):
        if item.type == 'weapon':
            if not self.can_use_item(item):
                return

            if self.hand is not None:
                self.inventory.add(self.hand)
            self.hand = item
            self.inventory.remove(item)

        elif item.type == 'armor':
            if not self.can_use_item(item):
                return

            if self.body is not None:
                self.inventory.add(self.body)
            self.body = item
            self.inventory.remove(item)

        elif item.type == 'consumable':
            self.hp += item.effect['hp']
            self.inventory.remove(item)

        else:
            print('Du kannst den Gegenstand nicht benutzen')

    def can_use_item(self, item):
        if item.lvl_req > self.level:
            print(f'Du musst mindestens Level {RED}{item.lvl_req}{NORMAL} sein um den Gegenstand benutzen zu können.')
            return False
        else:
            return True

    def pickup_loot(self, loot_table, *, loot_type=None):
        # some enemies have an empty loot table
        if loot_table is None:
            return

        # loot table is a list with lists inside it
        # inner list: [0] item
        #             [1] amount
        #             [2] chance

        if loot_type == 'fishing':  # only first item
            while True:
                loot = random.choice(loot_table)
                drop = loot[0]
                for i in range(loot[1]):
                    if random.random() <= loot[2]:
                        self.inventory.add(drop)
                        print(f'{ADDED} {drop.name}')
                        return

        else:
            for loot in loot_table:
                drop = loot[0]
                for i in range(loot[1]):
                    if random.random() <= loot[2]:
                        self.inventory.add(drop)
                        print(f'{ADDED} {drop.name}')

    def open_crafting(self):
        crafting_list = [
            Items.CookedMeat,
            Items.CookedFish,
            Items.SmallHealthPotion,
            Items.MediumHealthPotion,
            Items.HideArmor,
            Items.DragonhideArmor,
        ]

        visible_list = []
        for i in crafting_list:
            if i.crafting['visibility'] == 1:
                visible_list.append(i)
                continue
            for j in i.crafting['req']:
                for k in self.inventory:
                    if isinstance(k, j[0]):
                        visible_list.append(i)
                        break

        for i, crafting_result in enumerate(visible_list):
            print(f'{i + 1}| {UNDERLINED}{BOLD}{crafting_result.name}{NORMAL}')
            for j in crafting_result.crafting['req']:
                print(f'   - {j[1]}x {j[0].name}')
            print()

        choice = input_plus(f'Was willst du herstellen?\n{ENTER_LINE}')
        for i, crafting_result in enumerate(crafting_list):
            if choice == str(i + 1):
                self.craft_item(crafting_result)

    def craft_item(self, crafting_result):
        requirements = crafting_result.crafting['req']
        in_inventory = False
        for component in requirements:
            for i in self.inventory:
                if not isinstance(i, component[0]):
                    continue
                if self.inventory[i] >= component[1]:
                    in_inventory = True

        if not in_inventory:
            print(f'Dafür brauchst du:')
            for component in requirements:
                print(f'{component[1]}x {component[0].name}')
            return

        for component in requirements:
            for n in range(component[1]):
                self.inventory.remove(component[0]())
        self.inventory.add(crafting_result())
        print(f'Du hast {crafting_result.name} hergestellt')

    def fight_enemy(self, enemy):
        strong_enemy = RED if enemy.hp > self.hp_max else ''
        print(f'\nEin {BOLD}{strong_enemy}{enemy.name}{NORMAL} ist aufgetaucht.')

        while not enemy.hp <= 0:
            print(
                f'Der Gegner hat {enemy.hp} Lebenspunkte.\n'
                f'Du hast {self.hp} Lebenspunkte.\n\n'
                f'1| Gegner angreifen\n'
                f'2| Inventar öffnen\n'
                f'3| wegrennen')
            do = input_plus(f'Was willst du tun?\n')

            if do == '1':
                self.attack_enemy(enemy)
            elif do == '2':
                item = self.inventory.open()
                if item is not None:
                    self.use_item(item)
            elif do == '3':
                if random.choice([0, 1]) == 1:
                    print('Du bist entkommen.')
                    return False
                else:
                    print('Du hast es nicht geschafft zu entkommen.')
            else:
                continue

            if not enemy.hp <= 0:
                self.get_attacked(enemy)

        print(f'{BOLD}{strong_enemy}{enemy.name}{NORMAL} ist gestorben\n')
        self.receive_exp(enemy.ep_drop)
        self.add_gold(enemy.gold_drop)
        self.pickup_loot(enemy.loot_drop)
        return True
