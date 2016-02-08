import numpy as np
from ..vol_vispy_widget import QtVispyWidget
from ..options_widget import VolumeOptionsWidget
from glue.external.qt import get_qapp
from glue.core import Data


class KeyEvent(object):
    def __init__(self, text):
        self.text = text

class MouseEvent(object):
    def __init__(self, delta, type):
        self.type = type
        self.delta = delta

class TimerEvent(object):
    def __init__(self, type, iteration):
        self.type = type
        self.iteration = iteration

def test_widget():

    # Create fake data
    data = Data(primary=np.arange(1000).reshape((10,10,10)))

    # Set up widget
    w = QtVispyWidget()
    op = VolumeOptionsWidget(vispy_widget=w)
    w.data = data
    w.add_volume_visual()
    w.canvas.render()

    # Test timer
    w.on_timer(TimerEvent(type='timer_timeout', iteration=3))

    # Test key presses
    # w.on_key_press(KeyEvent(text='1'))
    # w.on_key_press(KeyEvent(text='2'))
    # w.on_key_press(KeyEvent(text='3'))

    # Test mouse_wheel
    w.on_mouse_wheel(MouseEvent(type='mouse_wheel', delta=(0, 0.5)))
    w.on_mouse_wheel(MouseEvent(type='mouse_wheel', delta=(0, -0.3)))
