# -*- coding: utf-8 -*-

import numpy as np


def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    z       A scalar or numpy array of any size.

    Return:
    s       sigmoid(z)
    """
    s = 1.0 / (1.0 + np.exp(-z))
    return s


def sigmoid_derivative(x):
    """
    Compute the derivative of the sigmoid function with respect to its input x.

    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    s = sigmoid(x)
    ds = s * (1.0 - s)
    return ds

