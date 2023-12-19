class foodStock:
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

    def updatedFood(self, food_stock, brought_food, consumed_food):
        """
        PRE : reçois en paramètre food_stock (int) à savoir la quantitée actuelle de nourriture dans la colonie
        ainsi que brougth_food (int), la quantitée de nourriture ramenée par la colonie
        POST : met à jour la quantitée actuelle de nourriture dans la colonie (int)
        """
        food_stock = food_stock + brought_food - consumed_food
        if food_stock < 0:
            food_stock = 0
        return food_stock

    def nbr_dead_ant(self, food_stock, consumed_food, ant_weight):
        """
        PRE : reçois en paramètre ;
            food_stock : la quantitée de nourriture dans la colonie (int)
            consumed_food : la quantitée de nourriture que la colonie vas consommer (int)
            ant_weight : le poids moyen d'une fourmis (int)
        POST : retourne le nombre de fourmis qui doivent mourrir (int)
        """
        nbrdeadant = (food_stock - consumed_food) * ant_weight / 2 * -1
        return nbrdeadant
