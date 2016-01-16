from vector import Vector
import logging

class Shape:
    def __init__(self):
        self.position = Vector(0, 0, 0)

    def intersections(self, vector, origin):
        raise NotImplementedError()

    def getColorAtPoint(self, point):
        raise NotImplementedError()

    def getNormalAtPoint(self, point):
        raise NotImplementedError()
