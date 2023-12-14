import classes.Basic_ant as BasicAnt
import classes.Queen_ant as QueenAnt
import classes.food as Food
import functions

if __name__ == "running.py" :

    nbrdeadant = 0
    day = day + 1
    Food.foodStock.updatedFood(Food.foodStock.manageFoodStock(ant_nbr, ant_weight))
    if food_stock - consumed_food < 0:
        nbrdeadant = (food_stock - consumed_food) * BasicAnt.ant_weight / 2 * -1
    manageAntTable(nbrdeadant)
    ant_nbr = len(ant_list)
    food_stock = food_stock - consumed_food
    if food_stock < 0:
        food_stock = 0
    if ant_nbr <= 0:
        ant_nbr = 0
        affichage()
        print("Toutes les fourmis sont mortes")
        break
    else:
        affichage()