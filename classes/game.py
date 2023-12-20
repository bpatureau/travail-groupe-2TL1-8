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
        day = day + 1
        consumed_food, brought_food = food.foodStock.manageFoodStock(ant_nbr, ant_weight)
        if food.foodStock.getFoodStock() - consumed_food <= 0:
            nbr_dead_ant = food.foodStock.nbr_dead_ant(food_stock, consumed_food, ant_weight)
            ant_hill.Ant_hill.killAnt(nbr_dead_ant)
        ant_nbr = len(ant_hill.Ant_hill.ant_alive())
        new_food_stock = food.foodStock.updatedFood()
        return day, ant_nbr, new_food_stock, consumed_food

    def hill_constructor(self, initial_ant_queen_nbr, initial_ant_nbr, day):
        """
        PRE : reçois en paramètre le nombre de reine et de fourmis voulu dans la colonie (int)
        POST : ajoute les fourmis dans la liste de ant_hill
        """
        for x in range(initial_ant_queen_nbr):
            ant_hill.Ant_hill.addQueen(day)
        for y in range(initial_ant_nbr):
            ant_hill.Ant_hill.addAnt(day)
