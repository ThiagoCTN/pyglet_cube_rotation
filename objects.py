import pyglet
from pyglet.gl import *
from models import Model

class Cube(Model):
    def __init__(self):
        cube = (
            1, 1, 1,    #0
            -1, 1, 1,   #1
            -1, -1, 1,  #2
            1, -1, 1,   #3
            1, 1, -1,   #4
            -1, 1, -1,  #5
            -1, -1, -1, #6
            1, -1, -1   #7
        )

        color = (
            1, 0, 0,
            1, 0, 0,
            1, 0, 0,
            1, 0, 0,
            0, 1, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 1
        )

        indice = (
            0, 1, 2, 3, # front face
            0, 4, 5, 1, # top face
            4, 0, 3, 7, # right face
            1, 5, 6, 2, # left face
            3, 2, 6, 7  # bottom face
            #4, 7, 6, 5 # back face
        )

        super().__init__(cube, color, indice)
