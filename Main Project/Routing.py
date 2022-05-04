class Routing:
    def __init__(self, name, stopsList):
        self.name = name
        self.stopsList = stopsList

    def getRoute(self):
        return self.stopsList
