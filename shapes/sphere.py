import math
from shapes.shape import Shape
from material import Material
import logging

log = logging.getLogger(__name__)

class Sphere(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def intersection(self, vector, origin):
        # Point on the ray is x = (origin + direction * distance)
        # Point on the sphere is mag(x - center)^2 = radius^2
        # Comibne to mag((origin + direction * distance) - center)^2 = radius^2
        # Solve for distance

        # determine coefficients of at^2 + bt + c
        a = (vector * vector)
        b = 2 * (vector * (origin - self.position))
        c = (origin - self.position) * (origin - self.position) - (self.radius ** 2)

        # discriminant
        d_sq = (b ** 2) - (4 * a * c)

        if d_sq < 0:
            return None

        d = math.sqrt(d_sq)
        t = (-b - d) / (2 * a)
        if t < 0:
            return None

        log.debug("{0} found intersection with {1}".format(self, vector))
        point = origin + (vector.normalized() * t)

        return t, point

    def getNormalAtPoint(self, point):
        return (point - self.position).normalized()

    def __repr__(self):
        return "Sphere(<{0.x}, {0.y}, {0.z}>, {1})".format(self.position, self.radius)
