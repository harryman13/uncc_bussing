from tkintermapview.canvas_position_marker import CanvasPositionMarker
from .Stops import Stop
import pandas as pd


class Bus(CanvasPositionMarker):
    def __init__(self, BusNumber, passengers, route, map_widget):
        self.route = route
        self.detailedRoute = []
        self.previousStop = route.iloc[0].at["Stop"]
        self.BusNumber = BusNumber
        self.nextStop = route.iloc[1].at["Stop"]
        self.previousStopTime = route.iloc[0].at["DateTime"]
        self.nextStopTime = route.iloc[1].at["DateTime"]
        self.passengers = passengers
        self.currentLine = 0
        super().__init__(map_widget = map_widget, position= self.getPos(0))

    def arrived(self):
        self.previousStop = self.nextStop
        self.previousStopTime = self.nextStopTime

    def getPos(self, index):
        return (self.route.iloc[index].at["Longitude"], self.route.iloc[index].at["Latitude"])

    def flatten(self):
        self.route.to_csv("Files/2407_b.csv")
        x = 0
        y = len(self.route)-1
        ind = 0
        while x < y:
            print("x:", x)
            print("y:", y)
            print(self.route.iloc[x].at["Stop"])
            print("stop: ", self.route.iloc[x].at["DateTime"])
            print("Count: ", self.route.iloc[x].at["Count"])
            print(self.route.iloc[x+1].at["Stop"])
            print("stop+1: ", self.route.iloc[x+1].at["DateTime"])
            print("Count+1: ", self.route.iloc[x+1].at["Count"])

            if (self.route.iloc[x].at["Stop"] == self.route.iloc[x+1].at["Stop"]):
                print("Stops Same")
                if (self.route.iloc[x+1].at["DateTime"] < (self.route.iloc[x].at["DateTime"] + pd.Timedelta(minutes= 3))):
                    print("Times Close")
                    if self.route.iloc[x+1].at["OnOff"] == "on":
                        self.route.at[ind,"Count"] = self.route.iloc[x + 1].at["Count"] - self.route.iloc[x].at["Count"]
                    else:
                        self.route.at[ind,"Count"] = self.route.iloc[x].at["Count"] - self.route.iloc[x+1].at["Count"]
                    self.route = self.route.drop(self.route.index[x+1])
                    y = y - 1
                    ind = ind + 1
            else:
                if self.route.iloc[x].at["OnOff"] == "off":
                    self.route.at[ind, "Count"] = (0 - self.route.iloc[x].at["Count"])
            x = x + 1
            ind = ind + 1

        #print("route:", self.route)
        print("Done")
        self.route.to_csv("Files/2407.csv")

    def update(self, time, dataframe):
        if time >= dataframe.loc[self.currentLine + 1].at["DateTime"]:
            self.currentLine = self.currentLine + 1
            self.previousStop = dataframe.loc[self.currentLine].at["Stop"]
            self.nextStop = dataframe.loc[self.currentLine + 1].at["Stop"]
            self.previousStopTime = dataframe.loc[self.currentLine].at["Time"]
            self.nextStopTime = dataframe.loc[self.currentLine + 1].at["Time"]
            if dataframe.loc[self.currentLine].at["OnOff"] == 'on':
                self.passengers = self.passengers + dataframe.loc[self.currentLine].at["Count"]
            else:
                self.passengers = self.passengers + dataframe.loc[self.currentLine].at["Count"]
        return 0
