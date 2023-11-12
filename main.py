# main

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

# class reineFourmis(fourmisGenerique):
#    def __init__(self, ):
#         super().__init__()
#        self

#     def __str__(self):
#        return super().__str__ + f""

    ant_list.append(Basic_ant(True, day, "oeuf"))  #reine à devenir
    for x in range(ant_nbr):
        ant_list.append(Basic_ant(True, day, "oeuf"))

    def manageFoodStock():
        nourritureRamenee = ant_nbr * 2.6
        nourritureConsommee = (ant_nbr * ant_weight) / 2
        return (nourritureConsommee, nourritureRamenee)

    def manageAntTable(nbrdeath):
        for ant in range(round(nbrBirth)):
            ant_list.append(Basic_ant(True, day, "oeuf"))
        for ant in range(round(nbrdeath)):
            if len(ant_list) > 1:
                ant_list.pop(1)
            else:
                ant_list.clear()


    def affichage():
        print(f"Jour : {day} \nFourmis dans la colonie : {ant_nbr} \n Nourriture de la colonie : {food_stock}\n nourriture consommée : {consumed_food}")

    while True:
        nbrdeadant = 0
        day = day + 1
        consumed_food, brought_food = manageFoodStock()
        food_stock = food_stock + brought_food
        if food_stock - consumed_food < 0:
            nbrdeadant = (food_stock - consumed_food)*ant_weight/2 * -1
        manageAntTable(nbrdeadant)
        ant_nbr = len(ant_list)
        food_stock = food_stock - consumed_food
        if food_stock < 0:
            food_stock = 0
        if ant_nbr <= 0:
            ant_nbr = 0
            affichage()
            print("Toutes les fourmis sont mortes")
            break
        else:
            affichage()

main(1100, 1, 6, 100, 2)
