import random


class Event:
    def __init__(self):
        pass

    def __str__(self):
        return "classe d'évènements aléatoires"

    def list_event(self, instance_food, instance_colony):
        prob = random.randint(0, 100)
        if 0 <= prob <= 50:
            instance_food._food_stock = instance_food.food_stock + len(instance_colony.ant_list)*1
        if 50 < prob <= 75:
            for x in range(round(prob/2)):
                instance_colony.killAnt()
        if 75 < prob <= 90:
            instance_food._food_stock = instance_food.food_stock - len(instance_colony.ant_list)*2
        if 90 < prob <= 95:
            for x in range(round(prob/1.5)):
                instance_colony.killAnt()
        if 95 < prob <= 99:
            instance_food._food_stock = instance_food.food_stock + len(instance_colony.ant_list)*5
        if prob == 100:
            for x in range(len(instance_colony.ant_list)):
                instance_colony.killAnt()
