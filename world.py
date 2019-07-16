import pyglet
from pyglet.gl import *
from objects import Cube

class World:
    def __init__(self):
        self.element = []

        self.addModel(Cube())

    def update(self, delta_time):
        for obj in self.element:
            obj.update(delta_time)

    def addModel(self, model):
        self.element.append(model)

    def draw(self):
        for obj in self.element:
            obj.draw()
