import classes.Ant_hill as ant_hill
import classes.food as food


class game:

    def __init__(self):
        pass

    def __str__(self):
        return ""

    def aDay(self, day, instance_food, instance_colony, ant_nbr, ant_weight):
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
        consumed_food, brought_food = instance_food.manageFoodStock(ant_nbr, ant_weight)
        if instance_food.food_stock - consumed_food <= 0:
            nbr_dead_ant = instance_food.nbr_dead_ant(consumed_food, ant_weight)
            for x in range(nbr_dead_ant):
                instance_colony.killAnt()
        instance_food.updatedFood(consumed_food, brought_food)
        return new_day, consumed_food
