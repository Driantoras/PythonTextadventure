import Enemies
import Items
from utilities import *
from vendor import Vendor
from ._abc import Location


class Mountain(Location):
    flavor_text = 'Während du den Weg entlang läufst\n' \
                  'siehst du einen Händler, der gerade an\n' \
                  'einem Lagerfeuer rastet.'

    vendor = Vendor('mountainVendor', 25, {
        Items.Apple(): 8, Items.Bread(): 6, Items.Mushroom(): 5,
        Items.RustySword(): 1, Items.IvoryHatchet(): 1
    }, f'"Hallo, ich bin ein Händler auf Reisen.\n'
       f' Schau dir ruhig meine Waren an."')

    golem_killed = False

    def __init__(self, player):
        super().__init__(player)
        self.items = [
            ['Händler ansprechen', self.talk_with_vendor, True],
            ['Fußspuren von Reptilien verfolgen', self.fight_lizard, True],
            ['Den Weg entlang laufen', self.walk_path, not self.golem_killed],
            ['Zum Steinbruch gehen', self.goto_quarry, self.golem_killed],
            ['Zum Wald gehen', self.goto_forest, True],
        ]

    def talk_with_vendor(self, player, questlog):
        self.vendor.talk_to(player)

    def fight_lizard(self, player, questlog):
        player.fight_enemy(Enemies.GiantLizard())

    def walk_path(self, player, questlog):
        print(
            f'Du läufst den Weg entlang und entdeckst am Ende\n'
            f'einen Steingolem, der den Weg versperrt. Du solltest\n'
            f'dich lieber vorbereiten bevor du in den Kampf gehst.\n')

        if input_plus(f'ja| Gegner angreifen?\n{ENTER_LINE}') == 'ja':
            if player.fight_enemy(Enemies.StoneGolem()):
                print(f'\nDu entdeckst hinter dem Haufen Steine der noch vom '
                      f'Steingolem übrig geblieben ist ein Steinbruch.')
                self.golem_killed = True

    def goto_quarry(self, player, questlog):
        return 'quarry'

    def goto_forest(self, player, questlog):
        return 'forest'
