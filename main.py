


# main

def main():
# définition globales

    food_stock = 10000
    queen_nbr = [1]
    ant_weight = 6
    ant_nbr = 1000
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
            if (counter - self.birth >= 10):
                self.isAlive = False

# class reineFourmis(fourmisGenerique):
#    def __init__(self, ):
#         super().__init__()
#        self

#     def __str__(self):
#        return super().__str__ + f""
    ant_list.append(Basic_ant(True, day, "oeuf"))  #reine à devenir
    for x in range(ant_nbr) :
        ant_list.append(Basic_ant(True, day, "oeuf"))

    def canEat():#une colonie mangera la moitié du poid de la colonie
        need2eat = ant_nbr * ant_weight / 2
        if need2eat < food_stock:
            return food_stock - need2eat
        else:
            for x in range((need2eat - food_stock) / ant_weight * 2):

                if ant_nbr > 1:
                    ant_nbr = ant_nbr - 1
                    ant_list.pop(1)
                elif ant_nbr == 1:
                    ant_list.pop(0)
                else:
                    print("Game Over")

    def getFood():
        stocknourriture = (ant_nbr * ant_weight) * 0.25


    def affichage():
        print(f"Jour : {day} \nFourmis dans la colonie : {ant_nbr} \n Nourriture de la colonie : {food_stock}")

    while ant_nbr > 0:
        day = day + 1
        canEat()
        getFood()
        affichage()
main()
