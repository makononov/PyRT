from vector import Vector
import math

class ImagePlane():
    def __init__(self):
        self.center = Vector(0, 0, 0)
        self.origin = Vector(0, 0, 0)
        self.width = 0
        self.height = 0

    def setDims(self, fov, dist, aspect):
        self.height = math.tan(fov) * dist * 2
        self.width = self.height * aspect
