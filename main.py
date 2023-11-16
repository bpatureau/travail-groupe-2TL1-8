# main
from random import random


def main(food_stock, queen_nbr, ant_weight, ant_nbr, nbrBirth):
# définition globales
    ant_list = []
    day = 0

    # définition de classe

    class Basic_ant:
        def __init__(self, isalive, birth, phase):
            self.isAlive = isalive
            self.birth = birth
            self.phase = phase

        def __str__(self):
            return "classe générique de fourmis."

        def isGonnaDie(self, counter):
            if (counter - self.birth >= 10):
                self.isAlive = False
    class Queen_ant(Basic_ant):
        def __init__(self, isalive, birth, phase):
         super().__init__(isalive, birth, phase)

        def __str__(self):
            return f"Reine"

    for queen in range(queen_nbr):
        ant_list.append(Queen_ant(True, 10, "adulte"))  #reine à devenir

    for x in range(ant_nbr):
        ant_list.append(Basic_ant(True, day, "oeuf"))

    def manageFoodStock():
        nourritureRamenee = ant_nbr * (random() + 1) * (foodmodifier * 2)
        nourritureConsommee = (ant_nbr * ant_weight) / 2
        return (nourritureConsommee, nourritureRamenee)
    def genRandomDeath():
        generatedrandomdeath = round((ant_nbr * (pow(2, random()) - 1) * 75 / 100))
        print(generatedrandomdeath)
        return generatedrandomdeath
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
        print(f"Jour : {day} \nFourmis dans la colonie : {ant_nbr} \n Nourriture de la colonie : {round(food_stock, 2)}g\n Nourriture consommée : {consumed_food}\n{displayant}\n{displayfood}")

    while True:
        input("press enter to continue")
        foodmodifier = 1
        displayant = ""
        displayfood = ""
        nbrdeadant = 0
        day = day + 1
        consumed_food, brought_food = manageFoodStock()
        food_stock = food_stock + brought_food
        if food_stock - consumed_food < 0:
            nbrdeadant = (food_stock - consumed_food)*ant_weight/2 * -1
        nbrdeadant += round(genRandomDeath())
        manageAntTable(nbrdeadant)
        ant_nbr = len(ant_list)
        food_stock = food_stock - consumed_food
        displayantfactor = round(ant_nbr / 2000 * 10)
        displayfoodfactor = round(food_stock / 7500 * 10)
        for ant in range(displayantfactor):
            displayant += "🐜"
        for food in range(displayfoodfactor):
            displayfood += "🥞"
        if food_stock < 0:
            food_stock = 0
        if ant_nbr <= 0:
            ant_nbr = 0
            affichage()
            print("Toutes les fourmis sont mortes")
            break
        else:
            affichage()

main(2000, 1, 6, 100, 300)
