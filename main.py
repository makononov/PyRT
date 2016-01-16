import pyglet
from scene import Scene
from camera import Camera
from shapes.sphere import Sphere
from vector import Vector

window = pyglet.window.Window()

camera = Camera()
camera.point_at = Vector(0, 0, -5)
scene = Scene(window.width, window.height, camera)

sphere = Sphere()
sphere.position = Vector(1, 1, -5)
sphere.radius = 1
sphere.material.color = (255, 0, 0)
scene.add(sphere)

vertex_list = []

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

pyglet.app.run()
