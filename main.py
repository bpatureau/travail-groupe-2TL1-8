######## définition globales ##########

nourriture = 10000
nbrReine = [1]
poidFourmisMg = 6
nbrFourmis = 1000
nbrFourmisListe = []

for x in range (nbrFourmis) :
    nbrFourmisListe[x] = x

######## définition de classe #########

class fourmisGenerique :
    def __init__(self, isAlive, naissance, phase) :
        self.isAlive = isAlive 
        self.naissance = naissance
        self.phase = phase

    def description(self) :
        return f"classe générique de fourmis."
    def __str__(self) :
        return self.description
    
    def isGonnaDie(self, compteur) :
        if (compteur - self.naissance >= 10 ) :
            self.isAlive = False
        return


class reineFourmis(fourmisGenerique) :
    def __init__(self, ) :
        super().__init__()
        self

    def __str__(self) :
        return super().__str__ + f""
    
###### fonctions #########

def canEat(nourriture) :             ##une colonie mangera la moitié du poid de la colonie 
    need2eat = (nbrFourmis * poidFourmisMg)/2
    if need2eat < nourriture :
        nourriture = nourriture - need2eat
    else :
        for x in range((need2eat - nourriture)/poidFourmisMg*2):
            nbrFourmis = nbrFourmis - 1
            nbrFourmisListe.pop(1)
    return
            
def getFood(nbrFourmis) :
    nourriture = (nbrFourmis * poidFourmisMg) * 0.25 
    return nourriture
        
###### main #######

def main() :
    jour = 0
    def affichage() :
        print(f"Jour : {jour} \nFourmis dans la colonie : {nbrFourmis} \n Nourriture de la colonie : {nourriture}")
    while nbrFourmis > 0 :
        jour = jour + 1
        canEat()
        getFood()
        affichage()
