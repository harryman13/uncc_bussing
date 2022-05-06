import pandas as pd

class Routing:
    def __init__(self, name):
        self.name = name
        self.stopsList = pd.DataFrame()

    def getRoute(self):
        return self.stopsList

    def addpoint(self, coordinate):
        self.stopsList = self.stopsList.append(coordinate)

