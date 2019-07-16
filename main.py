import sys
import pyglet
from window import Window

def main(*args, **kwargs):
    window = Window(fullscreen=False, vsync=True, resizable=True, 
                    height=600, width=600, caption="pyglet cube rotation")

    frames_per_second = 30.0
    pyglet.clock.schedule_interval(window.world.update, 1.0 / frames_per_second)
    pyglet.app.run()

if __name__ == "__main__":
    main(sys.argv)
