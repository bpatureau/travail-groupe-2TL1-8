import classes.Basic_ant
import classes.Queen_ant

def queenConstructor(queen_nbr):
    for queen in range(queen_nbr):
        ant_list.append(Queen_ant(True, 10, "adulte"))  # reine à devenir

def antConstructor(ant_nbr):
    for x in range(ant_nbr):
        ant_list.append(Basic_ant(True, day, "oeuf"))


def affichage():
    """
    PRE :
    POST : retourne un string contenant les statistiques actuelles de la colonie
    """
    print(
        f"Jour : {day} \nFourmis dans la colonie : {ant_nbr} \n Nourriture de la colonie : {food_stock}\n Nourriture consommée : {consumed_food}")
