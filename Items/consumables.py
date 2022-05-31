from ._abc import Consumable


class Apple(Consumable):
    name = 'Apfel'
    description = 'Ein roter Apfel'
    value = 1

    effect = {
        'hp': 10,
    }


class Bread(Consumable):
    name = 'Brot'
    description = 'Kann man Essen.'
    value = 2

    effect = {
        'hp': 15,
    }


class Mushroom(Consumable):
    name = 'Pilz'
    description = 'Nützlich für die Herstellung von Heiltränken.'
    value = 1

    effect = {
        'hp': 5,
    }


class RawMeat(Consumable):
    name = 'rohes Fleisch'
    description = 'Sollte zuerst gebraten werden bevor man es isst.'
    value = 3

    effect = {
        'hp': -10,
    }


class CookedMeat(Consumable):
    name = "gebratenes Fleisch"
    description = "Das ist Essen."
    value = 4

    effect = {
        'hp': 25,
    }
    crafting = {
        'visibility': 1,
        'req': [
            [RawMeat, 1],
        ]
    }


class RawFish(Consumable):
    name = 'roher Fisch'
    description = 'Sollte zuerst gebraten werden bevor man es isst.'
    value = 4

    effect = {
        'hp': -5,
    }


class CookedFish(Consumable):
    name = 'gebratener Fisch'
    description = 'Das ist Essen.'
    value = 5

    effect = {
        'hp': 25,
    }
    crafting = {
        'visibility': 1,
        'req': [
            [RawFish, 1],
        ]
    }


class SmallHealthPotion(Consumable):
    name = 'kleiner Heiltrank'
    description = 'Ein Trank um die Lebenspunkte wieder aufzufüllen.'
    value = 6
    lvl_req = 4

    effect = {
        'hp': 30,
    }
    crafting = {
        'visibility': 1,
        'req': [
            [Mushroom, 2],
        ]
    }


class MediumHealthPotion(Consumable):
    name = 'mittlerer Heiltrank'
    description = 'Ein Trank um die Lebenspunkte wieder aufzufüllen.'
    value = 10
    lvl_req = 8

    effect = {
        'hp': 50,
    }
    crafting = {
        'visibility': 1,
        'req': [
            [Mushroom, 2],
            [RawMeat, 1],
        ]
    }
