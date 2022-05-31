import Enemies
from utilities import *
from ._abc import Location


class Mine(Location):
    flavor_text = 'Du gehst in den spärlich ausgeleuchteten\n' \
                  'Minenschacht rein und siehst hin und \n' \
                  'wieder Blut und ein paar Knochen. Auf\n' \
                  'dem Boden erkennst du Fußspuren von\n' \
                  'Kobolden, manche sind viel größer als\n' \
                  'die anderen. Du entdeckst eine Abzweigung,\n' \
                  'die dunkel ist wo aber am Ende ein\n' \
                  'Licht flackert.'

    table_gold = True
    goblins_until_boss = 5
    goblin_boss_killed = False

    def __init__(self, player):
        super().__init__(player)
        self.items = [
            ['Dem Licht folgen', self.follow_light, self.table_gold],
            ['Dem Geräusch folgen', self.follow_sound, not self.goblin_boss_killed],
            ['Zum Steinbruch gehen', self.goto_quarry, True],
        ]

    def follow_light(self, player, questlog):
        print(f'Du findest einen Raum mit blutverschmierten Spitzhacken.')
        collect_mine_table_gold = input_plus(
            f'Auf dem Tisch neben an liegen ein paar Goldmünzen.\n'
            f'ja| Münzen mitnehmen?')
        if collect_mine_table_gold == 'ja':
            player.add_gold(17)
            self.table_gold = False
            player.fight_enemy(Enemies.Goblin())

    def follow_sound(self, player, questlog):
        conquer = True
        while conquer:
            if self.goblins_until_boss > 0:
                print(f'Ein Kobold kommt auf dich zu.')
                if player.fight_enemy(Enemies.Goblin()):
                    self.goblins_until_boss -= 1
                    if self.goblins_until_boss == 0:
                        print(f'Das müsste der letzte gewesen sein. '
                              f'Es ist nur noch dieser riesige Kobold übrig.')
            elif self.goblins_until_boss == 0:
                if player.fight_enemy(Enemies.GoblinKing()):
                    self.goblin_boss_killed = True
                    questlog.quests['quarry_goblins'].completed = True
                    return

            conquer = input_plus(f'ja| weitergehen?\n{ENTER_LINE}') == 'ja'

    def goto_quarry(self, player, questlog):
        return 'quarry'
