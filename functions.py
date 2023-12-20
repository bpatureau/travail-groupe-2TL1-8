def affichage(day, ant_nbr, food_stock, consumed_food):
    """
    PRE :
    POST : retourne un string contenant les statistiques actuelles de la colonie
    """
    print(
        f"Jour : {day} \nFourmis dans la colonie : {ant_nbr} \n Nourriture de la colonie : {food_stock}"
        f"\n Nourriture consommée : {consumed_food}")