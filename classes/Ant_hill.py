import sys

from . import Basic_ant
from . import Queen_ant
import random
import json
import os


class Ant_hill:

    def __init__(self):
        self.ant_list = []
        self.day = 0
        self.food = 0

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

    def save(self, fichier, food_stock, day):
        """
        PRE :
        POST :
        """
        all_data =[]
        colony_data = [day, food_stock]
        ant_data_liste = []

        for ant in self.ant_list:
            data = {
                "antClass": type(ant).__name__,
                "isAlive": ant.isAlive,
                "birth": ant.birth,
                "phase": ant.phase
            }
            ant_data_liste.append(data)

        all_data = [colony_data, ant_data_liste]

        path_courrant = os.getcwd()
        path_parent = os.path.dirname(path_courrant)
        path_save = path_parent + "/save/" + fichier
        path_save = fichier

        with open(path_save, "w") as file:
            json.dump(all_data, file, indent=4)

    def load(self, fichier):
        """
        PRE :
        POST :
        """
        path_courrant = os.getcwd()
        path_parent = os.path.dirname(path_courrant)
        path_save = path_parent + "/save/" + fichier
        path_save = fichier

        if not os.path.exists(path_save):
            print("Le fichier de sauvegarde n'existe pas.")
            return

        with open(path_save, "r") as file:
            all_data = json.load(file)

        ant_data_list = all_data[1]
        colony_data = all_data[0]
        self.day = colony_data[0]
        self.food = colony_data[1]

        for data in ant_data_list:
            ant_class_name = data["antClass"]
            is_alive = data["isAlive"]
            birth = data["birth"]
            phase = data["phase"]

            if ant_class_name == "Basic_ant":
                self.addAnt(birth)

            elif ant_class_name == "Queen_ant":
                self.addQueen(birth)

        print("Données chargées avec succès.")


#a = Ant_hill()
#a.hill_constructor(1, 25, 5)
#a.save("test2", 700, 5)
#print(a.ant_list)

#b = Ant_hill()
#b.load("test2")
#print(b.food)
#print(b.nbr_ant_alive())
#print(b.ant_list)



