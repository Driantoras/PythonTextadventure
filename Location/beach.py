import random
import time
from threading import Thread

import Enemies
import Items
from ._abc import Location


class Beach(Location):
    flavor_text = 'Du wachst an einem Strand auf und\n' \
                  'kannst dich an nichts mehr erinnern.'

    dead_body_loot = True
    cave_goblin = True

    def __init__(self, player):
        super().__init__(player)
        self.items = [
            ['Auf das Meer schauen', self.view_ocean, not isinstance(player.hand, Items.FishingRod)],
            ['Im Meer angeln', self.fishing, isinstance(player.hand, Items.FishingRod)],
            ['Leiche neben dir untersuchen', self.inspect_body, self.dead_body_loot],
            ['Die Höhle untersuchen', self.inspect_cave, self.cave_goblin],
            ['In den Wald laufen', self.goto_forest, True],
        ]

    def view_ocean(self, player, questlog):
        print(f'Du siehst dir das Meer an.\n')

    def fishing(self, player, questlog):
        print(f'Warten...')
        wait = FishingWaiter(random.randint(4, 7))
        wait.start()
        wait.join()  # thread waits to simulate fishing
        player.pickup_loot([
            [Items.RawFish(), 1, 0.9], [Items.Shoe(), 1, 0.1]
        ], loot_type='fishing')

    def inspect_body(self, player, questlog):
        player.pickup_loot([[Items.RustySword(), 1, 1]])
        self.dead_body_loot = False

    def inspect_cave(self, player, questlog):
        print(f'Du geht in die Höhle und wirst dabei von dem Bewohner bemerkt.')
        if player.fight_enemy(Enemies.Goblin()):
            self.cave_goblin = False

    def goto_forest(self, player, questlog):
        return 'forest'


class FishingWaiter(Thread):
    def __init__(self, seconds):
        Thread.__init__(self)
        self.seconds = seconds

    def run(self):
        time.sleep(self.seconds)
