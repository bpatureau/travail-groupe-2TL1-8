import classes.Basic_ant
import classes.Queen_ant
import random


class Ant_hill:

    def __init__(self):
        self.ant_list = []

    def __str__(self):
        return "colonie de fourmis"

    def ant_alive(self):
        return self.ant_list

    def addAnt(self):
        """
        PRE :
        POST : ajoute à la liste 'ant_list' une nouvelle instance Ant
        """
        newAnt = classes.Basic_ant
        self.ant_list.append(newAnt)

    def addQueen(self):
        """
        PRE :
        POST : ajoute à la liste 'ant_list' une nouvelle instance Queen_ant
        """
        newQueen = classes.Queen_ant
        self.ant_list.append(newQueen)

    def killAnt(self):
        """
        PRE :
        POST : enlève aléatoirement de la liste 'ant_list' une instance Ant
        """
        randomAnt = random.randint(0, len(self.ant_list))
        self.ant_list.pop(randomAnt)
