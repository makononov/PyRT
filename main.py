import pyglet
from scene import Scene
from camera import Camera
from shapes.sphere import Sphere
from shapes.plane import Plane
from light import PointLight
from vector import Vector
import logging
import color

window = pyglet.window.Window()
scene = None
last_drawn = -1
batch = pyglet.graphics.Batch()

vertex_list = []
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def initScene():
    global scene
    camera = Camera()
    camera.position = Vector(0, 1, 5)
    camera.point_at = Vector(0, 1, 0)
    scene = Scene(window.width, window.height, camera)
    log.info("Initialized scene with {0}x{1} image, {2}".format(window.width, window.height, camera))

    scene.ambient_light = color.scale(color.WHITE, 0.1)

    light = PointLight()
    light.position = Vector(5, 8, 8)
    log.info("Adding {0} to scene".format(light))
    scene.lights.append(light)

    light2 = PointLight()
    light2.position = Vector(-5, 8, 8)
    log.info("Adding {0} to scene".format(light2))
    scene.lights.append(light2)

    plane = Plane()
    plane.material.color = color.scale(color.WHITE, 0.5)
    plane.material.shininess = 0
    plane.material.reflection = 0.3
    log.info("Adding {0} to scene".format(plane))
    scene.shapes.append(plane)

    sphere = Sphere()
    sphere.position = Vector(1, 2, -3)
    sphere.radius = 1
    sphere.material.color = color.RED
    sphere.material.shininess = 30
    sphere.material.reflection = 0.7
    log.info("Adding {0} to scene".format(sphere))
    scene.shapes.append(sphere)

    sphere2 = Sphere()
    sphere2.position = Vector(-1, 1, -1.5)
    sphere2.radius = 1
    sphere2.material.color = color.YELLOW
    sphere2.material.shininess = 30
    sphere2.material.reflection = 0.7
    log.info("Adding {0} to scene".format(sphere2))
    scene.shapes.append(sphere2)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    global last_drawn
    log.debug(".")
    y = last_drawn + 1
    for x in range(window.width):
        batch.add(1,
                 pyglet.gl.GL_POINTS,
                 None,
                 ('v2i', (x, y)),
                 ('c3B', scene.getColorAt(x, y)))
    last_drawn = y
    if last_drawn == window.height:
        pyglet.clock.unschedule(update)

def main():
    log.info("Beginning log...")
    initScene()
    pyglet.clock.schedule(update)
    pyglet.app.run()

if __name__ == '__main__':
    main()
