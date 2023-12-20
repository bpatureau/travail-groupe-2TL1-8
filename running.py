import classes.Ant_hill as antHill
import classes.game as game
import classes.food as food
import functions

if True:

    """définition des variables initiales """

    day = 0
    ant_weight = 6
    food_stock = 5000
    initial_ant_queen_nbr = 1
    initial_ant_nbr = 300

    """création des instances"""

    runningGame = game.game()
    colony = antHill.Ant_hill()
    food = food.foodStock()
    food._food_stock = food_stock

    """création de la colonie"""

    colony.hill_constructor(initial_ant_queen_nbr, initial_ant_nbr, day)
    ant_nbr = colony.nbr_ant_alive()

    """boucle principale"""
    while colony.nbr_ant_alive() > 0:
        day, consumed_food = runningGame.aDay(day, food, colony, ant_nbr, ant_weight)
        functions.affichage(day, colony.nbr_ant_alive(), food.food_stock, consumed_food)

    """gui.main_menu(day, ant_nbr, food_stock, consumed_food)"""
