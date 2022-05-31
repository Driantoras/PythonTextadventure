import Items


class Enemy:
    name = ''
    hp = 1
    attack_damage = 1
    attack_speed = 1.0
    crit_rate = 0.1
    crit_multiplier = 1.5
    armor = None

    ep_drop = 0
    gold_drop = None
    loot_drop = None  # [[Item1, Amount, Chance], [Item2, Amount, Chance], ...]


class Bandit(Enemy):
    name = 'Räuber'
    hp = 100
    attack_damage = 16

    ep_drop = 80
    gold_drop = (17, 39)
    loot_drop = [
        [Items.Sabre(), 1, 1],
        [Items.Bread(), 3, 0.6],
    ]


class Boar(Enemy):
    name = 'Wildschwein'
    hp = 60
    attack_damage = 8
    attack_speed = 0.8

    ep_drop = 45
    loot_drop = [
        [Items.RawMeat(), 3, 0.6],
        [Items.Hide(), 2, 0.4],
    ]


class GiantLizard(Enemy):
    name = 'Riesenechse'
    hp = 65
    attack_damage = 7
    attack_speed = 1.2

    ep_drop = 60
    loot_drop = [
        [Items.RawMeat(), 2, 0.4],
        [Items.Hide(), 3, 0.7],
    ]


class Goblin(Enemy):
    name = 'Kobold'
    hp = 50
    attack_damage = 6
    attack_speed = 1.1

    ep_drop = 30
    gold_drop = (1, 8)
    loot_drop = [
        [Items.WoodenClub(), 1, 1],
        [Items.Bread(), 2, 0.8],
        [Items.Apple(), 2, 0.5],
    ]


class GoblinKing(Enemy):
    name = 'Koboldkönig'
    hp = 140
    attack_damage = 20
    attack_speed = 0.7

    ep_drop = 210
    gold_drop = (30, 40)
    loot_drop = [
        [Items.StoneMallet(), 1, 1],
        [Items.Bread(), 3, 0.4],
        [Items.CookedMeat(), 4, 0.7],
    ]


class StoneGolem(Enemy):
    name = 'Steingolem'
    hp = 120
    attack_damage = 18
    attack_speed = 0.6

    ep_drop = 150
    gold_drop = 50
