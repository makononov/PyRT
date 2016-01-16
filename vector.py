import math

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.coords = (x, y, z)

    def magnitude(self):
        return math.sqrt(sum([dim ** 2 for dim in self.coords]))

    def normalized(self):
        return self / self.magnitude()

    def dot(self, other):
        return sum([a * b for a,b in zip(self.coords, other.coords)])

    def theta_to(self, other):
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def cross(self, other):
        x = (self.coords[1] * other.coords[2]) - (other.coords[1] * self.coords[2])
        y = -((self.coords[0] * other.coords[2]) - (other.coords[0] * self.coords[2]))
        z = (self.coords[0] * other.coords[1]) - (other.coords[0] * self.coords[1])
        return Vector(x, y, z)

    def __add__(self, other):
        return Vector(*[a + b for a, b in zip(self.coords, other.coords)])

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Vector(*[x * other for x in self.coords])
        if type(other) is Vector:
            return self.dot(other)

    def __repr__(self):
        return "Vector({coords[0]}, {coords[1]}, {coords[2]})".format(coords=self.coords)

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return self * (1 / other)

    def __neg__(self):
        return Vector(*[-x for x in self.coords])

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __getattr__(self, attr):
        if (attr == 'x'):
            return self.coords[0]
        if (attr == 'y'):
            return self.coords[1]
        if (attr == 'z'):
            return self.coords[2]
        return super().__getattr__(attr)
