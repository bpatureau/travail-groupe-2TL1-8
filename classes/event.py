import random

class Event:
    def __init__(self):
        pass

    def __str__(self):
        return "classe d'évènements aléatoires"

    def list_event(self, food_stock, ant_nbr):
        prob = random.randint(0, 100)
        if 0 < prob < 50:
            pass
        if 50 < prob < 75:
            pass
        if 75 < prob < 90:
            pass
        if 90 < prob < 95:
            pass
        if 95 < prob < 99:
            pass
        if 99 < prob < 100:
            pass
