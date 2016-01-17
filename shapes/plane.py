from shapes.shape import Shape
from vector import Vector

class Plane(Shape):
    def __init__(self):
        super().__init__()
        self.normal = Vector(0, 1, 0)

    def intersection(self, vector, origin):
        if self.normal * vector == 0:
            # ray is parallel to plane
            return None

        w = origin - self.position
        dist = (-self.normal * w) / (self.normal * vector)
        if dist < 0:
            return None
        point = origin + (vector * dist)
        return dist, point

    def getNormalAtPoint(self, point):
        return self.normal

    def __repr__(self):
        return "Plane({0}), normal {1}".format(self.position, self.normal)
