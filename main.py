import pyglet
from scene import Scene
from camera import Camera
from shapes.sphere import Sphere
from light import PointLight
from vector import Vector
import logging
import color

window = pyglet.window.Window()
scene = None
vertex_list = []
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def initScene():
    global scene
    camera = Camera()
    camera.point_at = Vector(0, 0, -5)
    scene = Scene(window.width, window.height, camera)
    log.info("Initialized scene with {0}x{1} image, {2}".format(window.width, window.height, camera))

    scene.ambient_light = color.BLACK
    
    light = PointLight()
    scene.lights.append(light)

    sphere = Sphere()
    sphere.position = Vector(1, 1, -5)
    sphere.radius = 1
    sphere.material.color = color.RED
    log.info("Adding {0} to scene".format(sphere))
    scene.shapes.append(sphere)

    sphere2 = Sphere()
    sphere2.position = Vector(-1, -0.5, -4)
    sphere2.radius = 1
    sphere2.material.color = color.EAGLES_GREEN
    log.info("Adding {0} to scene".format(sphere2))
    scene.shapes.append(sphere2)

@window.event
def on_draw():
    window.clear()
    for x in range(window.width):
        batch = pyglet.graphics.Batch()
        for y in range(window.height):
            vertex_list.append(batch.add(1,
                                 pyglet.gl.GL_POINTS,
                                 None,
                                 ('v2i', (x, y)),
                                 ('c3B', scene.getColorAt(x, y))))
        batch.draw()

def main():
    log.info("Beginning log...")
    initScene()
    pyglet.app.run()

if __name__ == '__main__':
    main()
