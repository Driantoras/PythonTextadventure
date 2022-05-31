import Items
from utilities import *
from vendor import Vendor
from ._abc import Location


class Quarry(Location):
    flavor_text = 'Als du beim Steinbruch ankommst sieht\n' \
                  'du herumstehende Arbeiter.\n' \
                  'Manche von ihnen sind verletzt.'

    miner = Vendor('quarryMiner', 100, {
        Items.SmallHealthPotion(): 4, Items.Bread(): 10,
        Items.FishingRod(): 1, Items.LongSword(): 1
    })

    potion_for_worker = False

    def __init__(self, player):
        super().__init__(player)
        self.items = [
            ['Mit einem Arbeiter sprechen', self.talk_with_miner, True],
            ['Den verletzten Arbeitern einen Heiltrank geben', self.talk_to_injured, not self.potion_for_worker],
            ['Zum Bergpass gehen', self.goto_mountain, True],
            ['In die Mine gehen', self.goto_mine, True],
        ]

    def talk_with_miner(self, player, questlog):
        quest_quarry_goblins = questlog.quests['quarry_goblins']
        if not quest_quarry_goblins.activated:
            print(
                f'"Hallo, du siehst so aus als wärst du begabt mit dem\n'
                f' Umgang von Waffen. Kannst du uns helfen diese lästigen\n'
                f' Kobolde in der Mine vertreiben. Diese Biester stören uns\n'
                f' beim arbeiten. Wir würden dich dafür auch\n'
                f' angemessen belohnen."')
            quest_quarry_goblins.activated = True

        if quest_quarry_goblins.completed and not quest_quarry_goblins.reward_claimed:
            print(
                f'"Danke, dass uns von diesen Biestern befreit hast.\n'
                f' Hier ist deine Belohnung:"\n')
            player.add_gold(65)
            player.receive_exp(100)
            quest_quarry_goblins.reward_claimed = True

        self.miner.talk_to(player)

    def talk_to_injured(self, player, questlog):
        possible_healing_items = [Items.SmallHealthPotion, Items.MediumHealthPotion]
        has_healing = False
        for i, item in enumerate(possible_healing_items):
            if player.inventory[i] >= 1:
                print(f'{i + 1}| Arbeitern {BOLD}{item.name}{NORMAL} geben')
                has_healing = True

        if not has_healing:
            print(f'Du hast keinen Heiltrank dabei')
            return

        choice = input_plus(f'Entsprechende Zahl eingeben um den Gegenstand auszuwählen.\n{ENTER_LINE}')
        for i, item in enumerate(possible_healing_items):
            if choice == str(i + 1):
                player.inventory.remove(item)
                print(f'Du hast den Arbeitern {BOLD}{item.name}{NORMAL} gegeben')
                player.receive_exp(10 + (2 * item.value))

    def goto_mountain(self, player, questlog):
        return 'mountain'

    def goto_mine(self, player, questlog):
        return 'mine'
