from shapes.shape import Shape
from camera import Camera
from imageplane import ImagePlane
import random

class Scene:
    def __init__(self, image_width = 0, image_height = 0, cam = None):
        self.shapes = []
        if cam is None:
            self.camera = Camera()
        else:
            self.camera = cam

        self.image_width = image_width
        self.image_height = image_height

        self.image_plane = ImagePlane()
        self.image_plane.setDims(self.camera.fov, self.camera.focal_length, image_width / image_height)
        self.image_plane.center = self.camera.position - (self.camera.normal() * self.camera.focal_length)
        self.image_plane.origin = self.image_plane.center - (self.camera.u() * (self.image_plane.width / 2)) - (self.camera.v() * (self.image_plane.height / 2))

        self.background_color = (0, 0, 0)

    def add(self, shape):
        self.shapes.append(shape)

    def getColorAt(self, x, y):
        intersections = []
        for shape in self.shapes:
            shapeints = shape.intersections(self.getCameraRay(x, y), self.camera.position)
            intersections += [i for i in shapeints if i[0] > 0]
        try:
            t, point, shape = sorted(intersections, key = lambda i: i[0])[0]
            return shape.getColorAtPoint(point)
        except IndexError:
            return self.background_color

    def getPixelLocation(self, x, y):
        pixel_width = self.image_plane.width / self.image_width
        pixel_height = self.image_plane.height / self.image_height
        # Add 0.5 to pixel numbers to get center of pixel
        return self.image_plane.origin + (self.camera.u() * (x + 0.5) * pixel_width) + (self.camera.v() * (y + 0.5) * pixel_height)

    def getCameraRay(self, x, y):
        return (self.getPixelLocation(x, y) - self.camera.position).normalized()
