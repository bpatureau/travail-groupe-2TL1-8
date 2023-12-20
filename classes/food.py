class foodStock:
    def __init__(self):
        self._food_stock = 0

    def __str__(self):
        return "classe permettant de gérer la nourriture"

    @property
    def food_stock(self):
        return self._food_stock

    @food_stock.setter
    def food_stock(self, value):
        self._food_stock = value

    def manageFoodStock(self, ant_nbr, ant_weight):
        """
        PRE : reçois en paramètre ant_nbr (int) et ant_weight (int)
        POST : renvoie une quantitée (int) de nourriture ramenée ainsi qu'une quantitée (int) de nourriture consommée
        par la colonie
        """
        brought_food = ant_nbr * 2.6
        consumed_food = (ant_nbr * ant_weight) / 2
        return consumed_food, brought_food

    def updatedFood(self, consumed_food, brought_food):
        """
        PRE :
        POST : met à jour la quantitée actuelle de nourriture dans la colonie (int)
        """
        new_food_stock = self._food_stock + brought_food - consumed_food
        if new_food_stock < 0:
            self._food_stock = 0
        print(new_food_stock)
        self._food_stock = new_food_stock

    def nbr_dead_ant(self, consumed_food, ant_weight):
        """
        PRE : reçois en paramètre ;
            ant_weight : le poids moyen d'une fourmis (int)
        POST : retourne le nombre de fourmis qui doivent mourrir (int)
        """
        nbrdeadant = round((self.food_stock - consumed_food) * ant_weight / 2 * -1)
        return nbrdeadant
