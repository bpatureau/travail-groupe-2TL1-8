class food:
    def __init__(self):
        pass

    def __str__(self):
        return "classe permettant de gérer la nourriture"

    def manageFoodStock(self, ant_nbr, ant_weight):
        """
        PRE : reçois en paramètre ant_nbr (int) et ant_weight (int)
        POST : renvoie une quantitée (int) de nourriture ramenée ainsi qu'une quantitée (int) de nourriture consommée
        par la colonie
        """
        brought_food = ant_nbr * 2.6
        consumed_food = (ant_nbr * ant_weight) / 2
        return consumed_food, brought_food

    def updatedFood(self, food_stock, brought_food):
        """
        PRE : reçois en paramètre food_stock (int) à savoir la quantitée actuelle de nourriture dans la colonie
        ainsi que brougth_food (int), la quantitée de nourriture ramenée par la colonie
        POST : met à jour la quantitée actuelle de nourriture dans la colonie (int)
        """
        food_stock = food_stock + brought_food
        return food_stock

