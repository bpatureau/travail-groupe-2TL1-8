import classes.Ant_hill as antHill
import classes.game as game
import functions

if True:

    """définition des variables initiales """

    day = 0
    ant_weight = 6
    food_stock = 1000
    initial_ant_queen_nbr = 1
    initial_ant_nbr = 1000

    """création des instances"""

    runningGame = game.game()
    colony = antHill.Ant_hill()

    """création de la colonie"""

    colony.hill_constructor(initial_ant_queen_nbr, initial_ant_nbr, day)
    ant_nbr = colony.nbr_ant_alive()
    print(ant_nbr)

    """boucle principale"""

    day, ant_nbr, food_stock, consumed_food = runningGame.aDay(day, ant_nbr, food_stock, ant_weight)
    functions.affichage(day, ant_nbr, food_stock, consumed_food)
