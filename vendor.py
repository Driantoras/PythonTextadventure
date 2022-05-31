from utilities import *
from inventory import Inventory


class Vendor:
    def __init__(self, name, gold, items, text=''):
        self.name = name
        self.gold = gold
        self.inventory = Inventory(items)
        self.text = text

    def talk_to(self, player):
        if self.text:
            print(self.text)
        while True:
            choice = input_plus(
                f'1| Gegenstände verkaufen\n'
                f'2| Gegenstände kaufen\n'
                f'3| gehen')
            if choice == '1':
                item = self.open_trade(player, trade='sell')
                if item is not None:
                    self.player_sells_item(player, item)
            elif choice == '2':
                item = self.open_trade(player, trade='buy')
                if item is not None:
                    self.player_buys_item(player, item)
            elif choice == '3':
                break

    def open_trade(self, player, trade):
        print(f'Händler: {YELLOW}{self.gold}🪙{NORMAL}')
        player.print_gold()
        return self.inventory.open(trade=trade)

    def player_buys_item(self, player, item):
        if player.gold < item.value:
            print(f'Du hast nicht genug Gold um diesen Gegenstand zu kaufen.')
            return

        self.inventory.remove(item)
        player.inventory.add(item)
        player.gold -= item.value
        self.gold += item.value
        print(f'Du hast {item.value} Gold ausgegeben und {item.name} erhalten.')

    def player_sells_item(self, player, item):
        if self.gold < item.value:
            print(f'Der Händler hat nicht genug Gold\n')
            return

        player.inventory.remove(item)
        self.inventory.add(item)
        self.gold -= item.value
        player.gold += item.value
        print(f'Du hast dafür {item.value} Gold erhalten.')
