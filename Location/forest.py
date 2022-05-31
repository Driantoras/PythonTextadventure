import random
import time
from threading import Thread

import Enemies
import Items
from ._abc import Location
from utilities import *


class Forest(Location):
    flavor_text = 'Du gehst in den Wald hinein und sieht\n' \
                  'einen großen schwarzen Baum im Zentrum,\n' \
                  'der irgendwie besonders wirkt.'

    black_tree = True
    plants = True
    mountain_found = False

    def __init__(self, player):
        super().__init__(player)
        self.items = [
            ['Baum untersuchen', self.inspect_tree, self.black_tree],
            ['Baum angreifen', self.attack_tree, self.black_tree],
            ['Wald erkunden', self.explore, True],
            ['Wald durchsuchen', self.search, True],
            ['Zum Strand gehen', self.goto_beach, True],
            ['Zum Bergpass gehen', self.goto_mountain, self.mountain_found],
        ]

    def inspect_tree(self, player, questlog):
        print(f'Der Baum strahlt eine starke magische Aura aus,\n'
              f'du solltest ihn besser nicht angreifen.\n'
              f'Mit einem passenden Gegenstand könntest du\n'
              f'seine Macht extrahieren\n')

    def attack_tree(self, player, questlog):
        if player.hand is None:
            take_dmg = 10
            player.hp -= take_dmg
            print(
                f'Du hast mit der Faust gegen den Baum geschlagen und dir {BOLD}{take_dmg}{NORMAL} Schaden zugefügt.\n')

        elif isinstance(player.hand, Items.IvoryHatchet):
            print(f'Du hast den Baum gefällt.\n')

        else:
            player.hand = None
            print(f'Du hast mit deiner Waffe gegen den Baum geschlagen und somit deine Waffe zerstört.\n')

    def explore(self, player, questlog):
        print(f'Du erkundest den Wald...')
        wait = ExploreWaiter(random.randint(2, 5))
        wait.start()
        wait.join()

        found = False
        if self.mountain_found is False:
            if random.random() <= 0.3:
                found = True
        if found is True:
            self.mountain_found = True
            print(f'Du entdeckst einen Bergpass')
        else:
            print(f'Du hörst ein "{ITALIC}grunzen{NORMAL}", dass immer näher kommt.')
            player.fight_enemy(Enemies.Boar())

    def search(self, player, questlog):
        if not self.plants:
            print(f'Du musst etwas warten bis die Pflanzen nachgewachsen sind.')
            return

        player.pickup_loot([
            [Items.Apple(), 5, 0.5],
            [Items.Mushroom(), 3, 0.7],
        ])
        self.plants = False
        respawn_plants = RespawnPlants(60, self)
        respawn_plants.start()

    def goto_beach(self, player, questlog):
        return 'beach'

    def goto_mountain(self, player, questlog):
        return 'mountain'


class ExploreWaiter(Thread):
    def __init__(self, seconds):
        Thread.__init__(self)
        self.seconds = seconds

    def run(self):
        time.sleep(self.seconds)


class RespawnPlants(Thread):
    def __init__(self, seconds, area):
        Thread.__init__(self)
        self.seconds = seconds
        self.area = area

    def run(self):
        time.sleep(self.seconds)
        self.area.plants = True
