import pandas as pd

class Routing:
    def __init__(self, name):
        self.name = name
        self.stopsList = pd.DataFrame(columns = ['Lattitude','Longitude', 'isStop'])

    def getRoute(self):
        return self.stopsList

    def addPoint(self, lat, long, isStop):
        input = pd.Series({'Lattitude': lat, 'Longitude': long, 'isStop': isStop})

        self.stopsList = self.stopsList.append(input,ignore_index=True)

    def writeFile(self):
        self.stopsList.to_csv("Files/" + self.name + "DetailedBroke.csv")
        self.stopsList.to_csv("Files/" + self.name + "Detailed.csv")
