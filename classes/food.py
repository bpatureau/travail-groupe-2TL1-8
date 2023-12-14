class foodStock:
    def __init__(self):
        pass

    def __str__(self):
        return "classe permettant de gérer la nourriture"

    def manageFoodStock(self, ant_nbr, ant_weight):
        brought_food = ant_nbr * 2.6
        consumed_food = (ant_nbr * ant_weight) / 2
        return consumed_food, brought_food

    def updatedFood(self, food_stock, brought_food):
        food_stock = food_stock + brought_food
        return food_stock

