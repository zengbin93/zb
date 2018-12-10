# -*- coding: utf-8 -*-

"""
use pynput to monitor & control keyboard

Ref: https://pynput.readthedocs.io/en/latest/keyboard.html
====================================================================
"""

from pynput.keyboard import Key, Listener, Controller


class KeyboardMonitor:
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = "KEYBOARD MONITOR"

    @staticmethod
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    @staticmethod
    def on_release(key):
        print('{0} released'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False

    def run(self):
        with Listener(on_press=self.on_press,
                      on_release=self.on_release) as listener:
            listener.join()


KeyboardController = Controller


def run_keyboard_monitor():
    km = KeyboardMonitor()
    km.run()

