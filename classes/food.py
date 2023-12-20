class foodStock:
    def __init__(self, food_stock, brought_food, consumed_food):
        self.food_stock = food_stock
        self.brought_food = brought_food
        self.consumed_food = consumed_food

    def __str__(self):
        return "classe permettant de gérer la nourriture"

    def getFoodStock(self):
        return self.food_stock

    def manageFoodStock(self, ant_nbr, ant_weight):
        """
        PRE : reçois en paramètre ant_nbr (int) et ant_weight (int)
        POST : renvoie une quantitée (int) de nourriture ramenée ainsi qu'une quantitée (int) de nourriture consommée
        par la colonie
        """
        self.brought_food = ant_nbr * 2.6
        self.consumed_food = (ant_nbr * ant_weight) / 2
        return self.consumed_food, self.brought_food

    def updatedFood(self):
        """
        PRE :
        POST : met à jour la quantitée actuelle de nourriture dans la colonie (int)
        """
        self.food_stock = self.food_stock + self.brought_food - self.consumed_food
        if self.food_stock < 0:
            self.food_stock = 0
        return self.food_stock

    def nbr_dead_ant(self, ant_weight):
        """
        PRE : reçois en paramètre ;
            ant_weight : le poids moyen d'une fourmis (int)
        POST : retourne le nombre de fourmis qui doivent mourrir (int)
        """
        nbrdeadant = (self.food_stock - self.consumed_food) * ant_weight / 2 * -1
        return nbrdeadant