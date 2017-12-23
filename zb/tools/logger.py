# -*- coding: utf-8 -*-

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
    fh = logging.FileHandler(log_file)
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
