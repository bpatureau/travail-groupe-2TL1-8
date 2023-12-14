import classes.Basic_ant
import random


class Ant_hill:

    def __init__(self):
        self.ant_list = []

    def __str__(self):
        return "colonie de fourmis"

    def addAnt(self):
        newAnt = classes.Basic_ant
        self.ant_list.append(newAnt)

    def killAnt(self):
        randomAnt = random.randint(0, len(self.ant_list))
        self.ant_list.pop(randomAnt)
