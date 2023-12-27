import Basic_ant
import Queen_ant
import random
import json
import os


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
        newAnt = Basic_ant.Basic_ant(True, day, "adulte")
        self.ant_list.append(newAnt)

    def addQueen(self, day):
        """
        PRE :
        POST : ajoute à la liste 'ant_list' une nouvelle instance Queen_ant
        """
        newQueen = Queen_ant.Queen_ant(True, day, "adulte")
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

    def save(self, fichier):
        ant_data_liste = []

        for ant in self.ant_list:
            data = {
                "antClass": type(ant).__name__,
                "isAlive": ant.isAlive,
                "birth": ant.birth,
                "phase": ant.phase
            }
            ant_data_liste.append(data)

        path_courrant = os.getcwd()
        path = os.path.dirname(path_courrant)
        path_save = path + "/save/" + fichier

        with open(path_save, "w") as file:
            json.dump(ant_data_liste, file, indent=4)


a = Ant_hill()
a.hill_constructor(1, 20, 6)
print(type(a.ant_list[0]).__name__, (a.ant_list[0]).birth)

a.save("testo")


