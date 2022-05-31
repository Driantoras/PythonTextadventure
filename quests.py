from utilities import *

ICON_COMPLETED = f'{GREEN}{BOLD}X{NORMAL}'
ICON_OPEN = f'{YELLOW}{BOLD}?{NORMAL}'


class Quest:
    id = ''
    name = ''
    text = ''
    _activated = False
    _completed = False
    _reward_claimed = False

    @property
    def activated(self):
        return self._activated

    @activated.setter
    def activated(self, value):
        print(f'{YELLOW}Neuer Eintrag im Questlog{NORMAL}')
        self._activated = value

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        print(f'{ICON_COMPLETED} {BOLD}{self.name}{NORMAL}')
        self._completed = value

    @property
    def reward_claimed(self):
        return self._reward_claimed

    @reward_claimed.setter
    def reward_claimed(self, value):
        self._reward_claimed = value

    def __repr__(self):
        return f'{ICON_COMPLETED if self.completed else ICON_OPEN} - {BOLD}{self.name}{NORMAL}\n' \
               f'{" " * 4}{ITALIC}{self.text}{NORMAL}\n'


class QuarryGoblins(Quest):
    id = 'quarry_goblins'
    name = 'Bedrohung in der Mine'
    text = 'Befreie die Arbeiter in der Mine von den lästigen Kobolden.'


class Questlog:
    quests = {
        QuarryGoblins.id: QuarryGoblins(),
    }

    def list_quests(self):
        quests_available = False
        for quest in self.quests.values():
            if quest.activated:
                print(quest)
                quests_available = True

        if not quests_available:
            print('keine Quest angenommen')
