# -*- coding: utf-8 -*-

import functools
import time


# --------------------------------------------------------------------

def elapsed(func):
    """A decorator for calculating time elapsed when execute function"""

    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        print('Running `%s()` ...' % func.__name__)
        res = func(*args, **kw)
        end = time.time()
        print('Function `%s()` running elapsed %.2f s' %
              (func.__name__, end - start))
        return res

    return wrapper


# --------------------------------------------------------------------

def create_logger(log_file, name='logger', cmd=True):
    """define a logger for your program

    parameters
    ------------
    log_file     file name of log
    name         name of logger

    example
    ------------
    logger = create_logger('example.log',name='logger',)
    logger.info('This is an example!')
    logger.warning('This is a warn!')

    """
    import logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # set format
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    # file handler
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # cmd handler
    if cmd:
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
