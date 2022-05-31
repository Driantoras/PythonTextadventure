from ._abc import Ressource


class Hide(Ressource):
    name = 'Leder'
    description = 'Aus Tieren gewonnenes Leder.'
    value = 5


class Shoe(Ressource):
    name = 'Schuh'
    description = 'Nutzlos.'
    value = 0
