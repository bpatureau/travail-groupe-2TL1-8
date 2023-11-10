import random
def main():
# définition globales

    food_stock = 1000
    queen_nbr = [1]
    ant_weight = 6
    ant_nbr = 20
    ant_list = []
    day = 0

    # définition de classe

    class Basic_ant:
        def __init__(self, isalive, birth, phase):
            self.isAlive = isalive
            self.birth = birth
            self.phase = phase

        def description(self):
            return f"classe générique de fourmis."

        def __str__(self):
            return self.description

        def isGonnaDie(self, counter):
            if counter - self.birth >= 10:
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

    def canEat():
        reduced_food = ant_nbr * ant_weight / 2
        return reduced_food

    def getFood():
        added_food = (ant_nbr * ant_weight) * 0.3
        return added_food

    def killAnt(nbrdeath):
        alive_ant = []
        killed_ant = 0
        for ant in ant_list:
            if ant.isAlive:
                alive_ant.append(ant)
        for p in range(round(nbrdeath)):
            if len(alive_ant) > 1:
                ant_list[p].isAlive = False
                killed_ant += 1
        return killed_ant

    def reduceAnt():
        reduced_ant = (food_stock - consumed_food) * ant_weight / 2 * -1
        return reduced_ant

    def affichage():
        print(f"Jour : {day} \nFourmis dans la colonie : {ant_nbr} \nNourriture de la colonie : {food_stock} \nNourriture consomée : {consumed_food}")

    while True:
        day = day + 1
        consumed_food = canEat()
        founded_food = getFood()
        food_stock -= consumed_food
        if food_stock <= 0:
            nbrdeadant = reduceAnt()
            ant_nbr -= killAnt(nbrdeadant)
            food_stock = 0
        for element in ant_list:
            element.isGonnaDie(day)
        food_stock += founded_food
        ant_nbr -= killAnt(random.randint(0, 5))
        if ant_nbr <= 0:
            affichage()
            break
        affichage()

main()