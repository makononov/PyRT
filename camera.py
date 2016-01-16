from vector import Vector

class Camera:
    def __init__(self):
        super().__init__()
        self.position = Vector(0, 0, 0)
        self.point_at = Vector(0, 0, 0)
        self.focal_length = 1
        self.up = Vector(0, 1, 0)
        self.fov = 60

    def normal(self):
        return (self.position - self.point_at).normalized()

    def u(self):
        return self.up.cross(self.normal()).normalized()

    def v(self):
        return self.normal().cross(self.u()).normalized()

    def __repr__(self):
        return("Camera at {0}, pointing {1}".format(self.position, self.point_at))
