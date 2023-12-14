import classes.Basic_ant
import classes.Queen_ant

def queenConstructor(queen_nbr):
    for queen in range(queen_nbr):
        ant_list.append(Queen_ant(True, 10, "adulte"))  # reine à devenir

def antConstructor(ant_nbr):
    for x in range(ant_nbr):
        ant_list.append(Basic_ant(True, day, "oeuf"))


def manageFoodStock(ant_nbr, ant_weight):
    nourritureRamenee = ant_nbr * 2.6
    nourritureConsommee = (ant_nbr * ant_weight) / 2
    return (nourritureConsommee, nourritureRamenee)


def manageAntTable(nbrdeath):
    nbrQueen = 0
    for ant in ant_list:
        if isinstance(ant, Queen_ant):
            nbrQueen += 1
    for ant in range(round(nbrBirth)):
        for queen in range(nbrQueen):
            ant_list.append(Basic_ant(True, day, "oeuf"))
    for ant in range(round(nbrdeath)):
        if len(ant_list) > 1:
            ant_list.pop(1)
        else:
            ant_list.clear()


def affichage():
    print(
        f"Jour : {day} \nFourmis dans la colonie : {ant_nbr} \n Nourriture de la colonie : {food_stock}\n Nourriture consommée : {consumed_food}")
