# -*- coding: utf-8 -*-

import sys

class ProgressBar:
    """
    import time
    bar = ProgressBar(total = 10)
    for i in range(10):
        bar.move()
        bar.log()
        time.sleep(1)
    """

    def __init__(self, count=0, total=0, width=50):
        self.count = count
        self.total = total
        self.width = width

    def move(self):
        self.count += 1

    def log(self):
        sys.stdout.write('' * (self.width + 9) + '\r')
        sys.stdout.flush()
        progress = self.width * self.count / self.total
        sys.stdout.write('{0}/{1}: '.format(self.count, self.total))
        sys.stdout.write('#' * int(progress) + '-' * int(self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()
