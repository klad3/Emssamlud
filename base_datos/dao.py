# we expect every access to DB to be done through a class inherting from DAO

class DAO():
    def __init__(self, cursor):
        self._cursor = cursor
