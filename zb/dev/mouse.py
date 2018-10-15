# -*- coding: utf-8 -*-

"""
use pynput to monitor & control mouse

Ref: https://pynput.readthedocs.io/en/latest/mouse.html
====================================================================
"""


from pynput.mouse import Controller, Listener


class MouseMonitor:
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = "MOUSE MONITOR"

    @staticmethod
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    @staticmethod
    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False

    @staticmethod
    def on_scroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    def run(self):
        # Collect events until released
        with Listener(on_move=self.on_move, on_click=self.on_click,
                      on_scroll=self.on_scroll) as listener:
            listener.join()


MouseController = Controller

