import classes.Ant_hill as ant_hill
import classes.food as food


class game:

    def __init__(self):
        pass

    def __str__(self):
        return ""

    def aDay(self, day, ant_nbr, food_stock, ant_weight):
        """
        PRE : reçois les paramètres ;
            day : le jour actuel de la simulation (int)
            ant_nbr : le nombre de fourmis actuellement en vie dans la colonie (int)
            food_stock : la quantité actuelle de nourriture dans la colonie (int)
            ant_weight : le poids moyen d'une fourmis (int)
        POST : simule une journée type dans la colonie, met à jour et retourne les variables ;
             day : le nouveau jour actuel (int)
             ant_nbr : le nombre de fourmis dans la colonie mis à jour (int)
             new_food_stock : la quantitée mise a jour de nourriture dans la colonie (int)
        """
        new_day = day + 1
        food_stock = food.foodStock(food_stock)
        colony = ant_hill.Ant_hill()

        consumed_food, brought_food = food_stock.manageFoodStock(ant_nbr, ant_weight)
        if food_stock.getFoodStock() - consumed_food <= 0:
            nbr_dead_ant = food_stock.nbr_dead_ant(consumed_food, ant_weight)
            for x in range(nbr_dead_ant):
                colony.killAnt()
        new_ant_nbr = colony.nbr_ant_alive()
        new_food_stock = food_stock.updatedFood(consumed_food, brought_food)
        return new_day, new_ant_nbr, new_food_stock, consumed_food
