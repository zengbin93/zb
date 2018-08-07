# -*- coding: utf-8 -*-

import numpy as np


def euclidean_distant(vector1, vector2):
    """欧式距离"""
    vector1 = np.mat(vector1)
    vector2 = np.mat(vector2)
    return np.sqrt((vector1 - vector2) * (vector1 - vector2).T).item()


def manhattan_distant(vector1, vector2):
    """曼哈顿距离"""
    vector1 = np.mat(vector1)
    vector2 = np.mat(vector2)
    return np.sum(np.abs(vector1 - vector2))


def cosine_distant(vector1, vector2):
    """余弦距离"""
    vector1 = np.mat(vector1)
    vector2 = np.mat(vector2)
    vector1_norm = np.linalg.norm(vector1)
    vector2_norm = np.linalg.norm(vector2)
    dot_norm = vector1_norm * vector2_norm
    dot_vs = np.dot(vector1, vector2)
    return np.divide(dot_vs, dot_norm).item()


def pearson_similar(vector1, vector2):
    """皮尔逊相关系数"""
    if len(vector1) < 3:
        return 1.0
    return 0.5 + 0.5 * np.corrcoef(vector1, vector2, rowvar=0)[0][1]
