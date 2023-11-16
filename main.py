# main
from random import random


def main(food_stock, queen_nbr, ant_weight, ant_nbr, nbr_birth):
    # définition globales
    ant_list = []
    day = 0

    # définition de classe

    class BasicAnt:
        def __init__(self, isalive, birth, phase):
            self.isAlive = isalive
            self.birth = birth
            self.phase = phase

        def __str__(self):
            return "classe générique de fourmis."

        def is_gonna_die(self, counter):
            if counter - self.birth >= 10:
                self.isAlive = False

    class QueenAnt(BasicAnt):
        def __init__(self, isalive, birth, phase):
            super().__init__(isalive, birth, phase)

        def __str__(self):
            return f"Reine"

    for queen in range(queen_nbr):
        ant_list.append(QueenAnt(True, 10, "adulte"))  # reine à devenir

    for x in range(ant_nbr):
        ant_list.append(BasicAnt(True, day, "oeuf"))

    def manage_food_stock():
        nourriture_ramenee = ant_nbr * (random() + 1) * (foodmodifier * 2)
        nourriture_consommee = (ant_nbr * ant_weight) / 2
        return nourriture_consommee, nourriture_ramenee

    def gen_random_death():
        generatedrandomdeath = round((ant_nbr * (pow(2, random()) - 1) * 75 / 100))
        return generatedrandomdeath

    def manage_ant_table(nbrdeath):
        nbr_queen = 0
        for ant in ant_list:
            if isinstance(ant, QueenAnt):
                nbr_queen += 1
        for ant in range(round(nbr_birth)):
            for queen in range(nbr_queen):
                ant_list.append(BasicAnt(True, day, "oeuf"))
        for ant in range(round(nbrdeath)):
            if len(ant_list) > 1:
                ant_list.pop(1)
            else:
                ant_list.clear()

    def affichage(message):
        print(message)
        input("press enter to continue")

    while True:

        foodmodifier = 1
        displayant = ""
        displayfood = ""
        nbrdeadant = 0
        day = day + 1
        consumed_food, brought_food = manage_food_stock()
        food_stock = food_stock + brought_food
        if food_stock - consumed_food < 0:
            nbrdeadant = (food_stock - consumed_food) * ant_weight / 2 * -1
        nbrdeadant += round(gen_random_death())
        manage_ant_table(nbrdeadant)
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
            affichage("Toutes les fourmis sont mortes")
            break
        else:
            affichage(f"Jour : {day} \nFourmis dans la colonie : {ant_nbr} \n"
            f"Nourriture de la colonie : {round(food_stock, 2)}g\nNourriture consommée : {consumed_food}\n"
            f"{displayant}\n{displayfood}")
main(2000, 1, 6, 100, 300)
