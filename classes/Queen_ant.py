from . import Basic_ant


class Queen_ant(Basic_ant.Basic_ant):
    def __init__(self, isalive, birth, phase):
        super().__init__(isalive, birth, phase)

    def __str__(self):
        return f"Reine"
