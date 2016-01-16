import math
from shapes.shape import Shape
from material import Material

class Sphere(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 0
        self.material = Material()

    def intersections(self, vector, origin):
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

        intersections = []

        if d_sq >= 0:
            # one or two intersections
            d = math.sqrt(d_sq)
            dists = [(-b + d) / (2 * a)]
            if d > 0:
                dists.append((-b - d) / (2 * a))

            for t in dists:
                point = origin + (vector.normalized() * t)
                intersections.append((t, point, self))

        return intersections

    def getColorAtPoint(self, point):
        return self.material.color
