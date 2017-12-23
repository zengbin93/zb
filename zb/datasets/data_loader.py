# -*- coding: utf-8 -*-

"""
加载数据集
"""
import pandas as pd


def load_iris():

    # The “Iris” dataset  https://archive.ics.uci.edu/ml/datasets/Iris
    path = 'https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv'
    iris = pd.read_csv(path)
    return iris

def load_milk_productions():
    # Monthly milk production: pounds per cow. Jan 62 – Dec 75[Edit]
	path = 'milk-productions.csv'
    mps = pd.read_csv(path)
    return mps

