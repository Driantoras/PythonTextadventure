from collections import Counter

from utilities import *


class Inventory(Counter):

    def add(self, item):

        if item.stackable:
            for i in self:
                if i.name == item.name:
                    self[i] += 1
                    return
            else:
                self[item] += 1

        elif not item.stackable:
            self[item] = 1

    def remove(self, item):

        if item.stackable:
            self[item] -= 1
            if self[item] == 0:
                del self[item]

        elif not item.stackable:
            del self[item]

    def open(self, trade=None):

        if not len(self):
            if trade == 'buy':
                print('Der Händler hat keine Waren dabei')
            else:
                print('Du hast keine Gegenstände in deinen Taschen\n')
            return

        if trade == 'buy':
            print(f'Gegenstände des Händlers:')
        else:
            print(f'Diese Gegenstände hast du dabei:')

        for i, item in enumerate(self):
            name = f'[{self[item]}x] {item.name}' if item.stackable else item.name
            print(f"{i + 1}| {name}")

        choice = input_plus(
            f'Entsprechende Zahl eingeben um '
            f'den Gegenstand auszuwählen.\n{ENTER_LINE}')

        for i, item in enumerate(self):
            if choice == str(i + 1):
                print(repr(item))

                if trade:
                    buy_or_sell = 'verkaufen' if trade == 'sell' else 'kaufen'
                    if input_plus(f'ja| Gegenstand für {item.value} Gold {buy_or_sell}?\n{ENTER_LINE}') == 'ja':
                        return item
                else:
                    print(f'ja| Gegenstand benutzen/ausrüsten?')
                    if input_plus(f'{ENTER_LINE}') == 'ja':
                        return item
