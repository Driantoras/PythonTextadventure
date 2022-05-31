from ._abc import Weapon


class RustySword(Weapon):
    name = 'rostiges Schwert'
    description = 'Ein stark verrostetes Schwert.'
    value = 8
    lvl_req = 1

    attack_damage = 10
    attack_speed = 1
    crit_rate = 0.05
    crit_multiplier = 1.7


class WoodenClub(Weapon):
    name = 'Holzknüppel'
    description = 'Eine Keule aus Holz. Sehr primitiv.'
    value = 5
    lvl_req = 1

    attack_damage = 10
    attack_speed = 0.8
    crit_rate = 0.04
    crit_multiplier = 1.5


class StoneMallet(Weapon):
    name = 'Steinblockhammer'
    description = 'Großer Stein am Stock'
    value = 4
    lvl_req = 7

    attack_damage = 15
    attack_speed = 0.5
    crit_rate = 0.08
    crit_multiplier = 1.2


class LongSword(Weapon):
    name = 'Langschwert'
    description = 'Ein langes Schwert. Gute Reichweite und Schneidigkeit'
    value = 29
    lvl_req = 10

    attack_damage = 18
    attack_speed = 0.8
    crit_rate = 0.1
    crit_multiplier = 1.5


class Sabre(Weapon):
    name = 'Säbel'
    description = 'Nur für echte Piraten. *arrgghh*'
    value = 25
    lvl_req = 5

    attack_damage = 15
    attack_speed = 1.3
    crit_rate = 0.1
    crit_multiplier = 1.8


class IvoryHatchet(Weapon):
    name = 'Elfenbeinaxt'
    description = 'Leuchtet weiß. Besteht aus Beinen von Elfen.'  # TODO Area mit Elfen die das nicht mögen und dich angreifen wenn du es in der Hand hast
    value = 40
    lvl_req = 1

    attack_damage = 12
    attack_speed = 1
    crit_rate = 0.1
    crit_multiplier = 1.5


class FishingRod(Weapon):
    name = 'Angelrute'
    description = 'Stock mit Schnur. Damit kann man Sachen aus Gewässern ziehen.'
    value = 30
    lvl_req = 6

    attack_damage = 5
    attack_speed = 0.5
    crit_rate = 0.1
    crit_multiplier = 1.5


class Dolch(Weapon):
    name = 'Dolch'
    description = 'Für hinterlistige Angelegenheiten gut geeignet.'
    value = 32
    lvl_req = 12

    attack_damage = 13
    attack_speed = 1.8
    crit_rate = 0.2
    crit_multiplier = 2.2
