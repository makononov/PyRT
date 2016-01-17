from vector import Vector
from material import Material
import logging

class Shape:
    def __init__(self):
        self.position = Vector(0, 0, 0)
        self.material = Material()

    def intersection(self, vector, origin):
        raise NotImplementedError()

    def getColorAtPoint(self, point):
        return self.material.color

    def getNormalAtPoint(self, point):
        raise NotImplementedError()
