from shapes.shape import Shape
import logging
import color
from camera import Camera
from imageplane import ImagePlane
import random

log = logging.getLogger(__name__)

class Scene:
    def __init__(self, image_width = 0, image_height = 0, cam = None):
        self.shapes = []
        self.lights = []

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

        self.background_color = color.BLACK
        self.ambient_light = color.scale(color.WHITE, 0.2)
        log.info("Scene initialized")


    def getColorAt(self, x, y):
        intersection = None
        log.debug("Firing ray through ({0}, {1})".format(x, y))
        ray = self.getCameraRay(x,y)
        for shape in self.shapes:
            try:
                t, point = shape.intersection(ray, self.camera.position)
            except TypeError:
                continue

            if intersection is None or t < intersection[0]:
                intersection = (t, point, shape)

        if intersection:
            return self.calculateShading(intersection)

        return self.background_color

    def getPixelLocation(self, x, y):
        pixel_width = self.image_plane.width / self.image_width
        pixel_height = self.image_plane.height / self.image_height
        # Add 0.5 to pixel numbers to get center of pixel
        return self.image_plane.origin + (self.camera.u() * (x + 0.5) * pixel_width) + (self.camera.v() * (y + 0.5) * pixel_height)

    def getCameraRay(self, x, y):
        return (self.getPixelLocation(x, y) - self.camera.position).normalized()

    def calculateShading(self, intersection):
        point = intersection[1]
        shape = intersection[2]
        normal = shape.getNormalAtPoint(point)
        shapeColor = shape.getColorAtPoint(point)
        log.debug("Shading {0} {1}".format(shape, point))

        # ambient portion
        result = color.component_scale(shapeColor, [x/255 for x in self.ambient_light])

        for light in self.lights:
            # shadow
            lightDir = (light.position - point).normalized()
            lightDist = (light.position - point).magnitude()
            shadowed = False
            for shape in self.shapes:
                try:
                    dist, point = shape.intersection(lightDir, point + (normal * 0.001))
                    if dist <= lightDist:
                        shadowed = True
                        log.debug("Shadowed by {0} at distance {1}".format(shape, dist))
                        break
                except TypeError:
                    pass

            if not shadowed:
                # diffuse
                diffIntensity = min(max(lightDir * normal, 0), 1)
                diff = color.scale(light.color, diffIntensity)
                diff = color.component_scale(shapeColor, [x/255 for x in diff])
                log.debug("Diff: {0} (intensity {1})".format(diff, diffIntensity))
                result = color.add(result, diff)

                # blinn-phong
                if diffIntensity > 0:
                    viewDir = -(point - self.camera.position).normalized()
                    halfDir = (lightDir + viewDir).normalized()
                    specAngle = min(max(halfDir * normal, 0), 1)
                    specIntensity = specAngle ** shape.material.shininess
                    spec = color.scale(light.color, specIntensity)
                    result = color.add(result, spec)

        return result
