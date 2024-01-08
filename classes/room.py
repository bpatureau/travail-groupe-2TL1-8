class Room:
    def __init__(self, name, location, size):
        self._name = name
        self._location = location
        self._size = size
    @property
    def name(self):
        return self._name
    def get_location(self):
        return self._location
    def get_size(self):
        return self._size