from .canvas_position_marker import CanvasPositionMarker


class Stop(CanvasPositionMarker):
    def __init__(self, routeList, routePassengers, timesNextPickup, timesLastPickup, nextPickupPassengers):
        self.routeList = routeList
        self.routePassengers = routePassengers
        self.timesNextPickup = timesNextPickup
        self.timesLastPickup = timesLastPickup
        self.nextPickupPassengers = nextPickupPassengers







