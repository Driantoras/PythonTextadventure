from .beach import Beach
from .forest import Forest
from .mine import Mine
from .mountain import Mountain
from .quarry import Quarry


def create(player):
    return {
        'beach': Beach(player),
        'forest': Forest(player),
        'mountain': Mountain(player),
        'quarry': Quarry(player),
        'mine': Mine(player),
    }
