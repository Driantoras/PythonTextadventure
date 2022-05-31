from ._abc import Armor
from .ressources import Hide


class HideArmor(Armor):
    name = 'Lederrüstung'
    description = 'Eine aus Leder gefertigte Rüstung.'
    value = 15
    lvl_req = 5

    armor = 20
    crafting = {
        'visibility': 1,
        'req': [
            [Hide, 5],
        ]
    }


class DragonhideArmor(Armor):
    name = 'Drachenlederrüstung'
    description = ''
    value = 360
    lvl_req = 30

    armor = 80

    crafting = {
        'visibility': 2,
        'req': [
            # dragon hide + magic stuff
        ]
    }
