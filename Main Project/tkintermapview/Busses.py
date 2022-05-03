from .canvas_position_marker import CanvasPositionMarker
from .Stops import Stop
import pandas as p
import QueryFunctions.py

class Bus(CanvasPositionMarker):
    def __init__(self, BusNumber, previousStop, nextStop, previousStopTime, nextStopTime, passengers):
        self.previousStop = previousStop
        self.nextStop = nextStop
        self.previousStopTime = previousStopTime
        self.nextStopTime = nextStopTime
        self.passengers = passengers

    def arrived(self):
        self.previousStop = self.nextStop
        self.previousStopTime = self.nextStopTime

    def update(self, time, dataframe, lineNumber):
        self.previousStop = dataframe.loc[lineNumber].at["Stop"]
        self.nextStop = dataframe.loc[lineNumber + 1].at["Stop"]
        self.previousStopTime = dataframe.loc[lineNumber].at["Time"]
        self.nextStopTime = dataframe.loc[lineNumber + 1].at["Time"]