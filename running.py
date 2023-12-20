import classes.Ant_hill as antHill
import classes.game as game
import functions

if __name__ == "running.py":

    """définition des variables initiales """

    day = 0
    ant_weight = 6
    food_stock = 1000
    initial_ant_queen_nbr = 1
    initial_ant_nbr = 1000
    runningGame = game.game()

    """création de la colonie"""

    runningGame.hill_constructor(initial_ant_queen_nbr, initial_ant_nbr, day)
    colony = antHill.Ant_hill()
    ant_nbr = len(colony.ant_alive())

    """boucle principale"""

    if input("press enter"):
        day, ant_nbr, food_stock, consumed_food = runningGame.aDay(day, ant_nbr, food_stock, ant_weight)
        functions.affichage(day, ant_nbr, food_stock, consumed_food)
