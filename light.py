import color
from vector import Vector

class Light:
    def __init__(self):
        self.color = color.WHITE

class PointLight(Light):
    def __init__(self):
        super().__init__()
        self.position = Vector(0, 0, 0)

    def __repr__(self):
        return "PointLight({0.x}, {0.y}, {0.z}), Color {1}".format(self.position, self.color)
