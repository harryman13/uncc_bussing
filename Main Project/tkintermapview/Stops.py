from .canvas_position_marker import CanvasPositionMarker


class Stop(CanvasPositionMarker):
    def __init__(self, routeList, routePassengers, timesNextPickup, timesLastPickup, nextPickupPassengers):
        self.routeList = routeList
        self.routePassengers = routePassengers
        self.timesNextPickup = timesNextPickup
        self.timesLastPickup = timesLastPickup
        self.nextPickupPassengers = nextPickupPassengers

    def update(self, time, dataframe, lineNumber):
        if time >= dataframe.loc[lineNumber + 1].at["Time"]:
            if dataframe.loc[lineNumber].at["Route"] == "Gold":
                self.routePassengers[0] = dataframe.loc[lineNumber].at["Count"]
                self.timesLastPickup[0] = dataframe.loc[lineNumber].at["Time"]
                self.timesNextPickup[0] = dataframe.loc[lineNumber + 1].at["Time"]
                self.nextPickupPassengers[0] = dataframe.loc[lineNumber + 1].at["Count"]
            if dataframe.loc[lineNumber].at["Route"] == "Green":
                self.routePassengers[1] = dataframe.loc[lineNumber].at["Count"]
                self.timesLastPickup[1] = dataframe.loc[lineNumber].at["Time"]
                self.timesNextPickup[1] = dataframe.loc[lineNumber + 1].at["Time"]
                self.nextPickupPassengers[1] = dataframe.loc[lineNumber + 1].at["Count"]
            if dataframe.loc[lineNumber].at["Route"] == "Silver":
                self.routePassengers[2] = dataframe.loc[lineNumber].at["Count"]
                self.timesLastPickup[2] = dataframe.loc[lineNumber].at["Time"]
                self.timesNextPickup[2] = dataframe.loc[lineNumber + 1].at["Time"]
                self.nextPickupPassengers[2] = dataframe.loc[lineNumber + 1].at["Count"]
        return 0






