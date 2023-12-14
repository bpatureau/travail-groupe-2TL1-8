class Basic_ant:
    def __init__(self, isalive, birth, phase):
        self.isAlive = isalive
        self.birth = birth
        self.phase = phase

    def __str__(self):
        return "classe générique de fourmis."

    def isGonnaDie(self, counter):
        if counter - self.birth >= 10:
            self.isAlive = False