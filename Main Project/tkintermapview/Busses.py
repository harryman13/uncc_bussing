from .canvas_position_marker import CanvasPositionMarker
from .Stops import Stop


class Bus(CanvasPositionMarker):
    def __init__(self, previousStop, nextStop, previousStopTime, nextStopTime, passengers):
        self.previousStop = previousStop
        self.nextStop = nextStop
        self.previousStopTime = previousStopTime
        self.nextStopTime = nextStopTime
        self.passengers = passengers

    def arrived(self):
        self.previousStop = self.nextStop
        self.previousStopTime = self.nextStopTime
