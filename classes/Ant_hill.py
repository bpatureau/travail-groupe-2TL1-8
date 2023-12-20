import classes.Basic_ant
import classes.Queen_ant
import random


class Ant_hill:

    def __init__(self):
        self.ant_list = []

    def __str__(self):
        return "colonie de fourmis"

    def nbr_ant_alive(self):
        return len(self.ant_list)

    def addAnt(self, day):
        """
        PRE :
        POST : ajoute à la liste 'ant_list' une nouvelle instance Ant
        """
        newAnt = classes.Basic_ant.Basic_ant(True, day, "adulte")
        self.ant_list.append(newAnt)

    def addQueen(self, day):
        """
        PRE :
        POST : ajoute à la liste 'ant_list' une nouvelle instance Queen_ant
        """
        newQueen = classes.Queen_ant.Queen_ant(True, day, "adulte")
        self.ant_list.append(newQueen)

    def killAnt(self):
        """
        PRE :
        POST : enlève aléatoirement de la liste 'ant_list' une instance Ant
        """
        randomAnt = random.randint(0, len(self.ant_list))
        try:
            if len(self.ant_list) > 0:
                self.ant_list.pop(randomAnt)
        except IndexError:
            print("no more ants")

    def hill_constructor(self, initial_ant_queen_nbr, initial_ant_nbr, day):
        """
        PRE : reçois en paramètre le nombre de reine et de fourmis voulu dans la colonie (int)
        POST : ajoute les fourmis dans la liste de ant_hill
        """
        for x in range(initial_ant_queen_nbr):
            self.addQueen(day)
        for y in range(initial_ant_nbr):
            self.addAnt(day)
