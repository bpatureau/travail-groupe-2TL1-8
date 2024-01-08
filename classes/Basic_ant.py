class Basic_ant:
    def __init__(self, isalive, birth, phase):
        self.isAlive = isalive
        self._birth = birth

        self.phase = phase

    @property
    def get_isAlive(self):
        return self._isAlive

    def __str__(self):
        return "classe générique de fourmis."
    @property
    def birth(self):
        return self._birth
    def isGonnaDie(self, day):
        if day - self.birth >= 10:
            self._isAlive = False
