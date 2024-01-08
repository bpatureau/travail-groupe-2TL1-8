class Basic_ant:
    def __init__(self, isalive, birth, phase):
        self._isAlive = isalive
        self.birth = birth
        self.phase = phase

    @property
    def get_isAlive(self):
        return self._isAlive

    def __str__(self):
        return "classe générique de fourmis."

    def isGonnaDie(self, day):
        if day - self.birth >= 10:
            self._isAlive = False
