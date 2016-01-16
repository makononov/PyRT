import color
from vector import Vector

class Light:
    def __init__(self):
        self.color = color.WHITE

class PointLight(Light):
    def __init__(self):
        super().__init__()
        self.position = Vector(0, 0, 0)
