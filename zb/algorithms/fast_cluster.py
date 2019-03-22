# -*- coding: utf-8 -*-
"""

Reference:
1. https://github.com/jasonwbw/DensityPeakCluster
2. Rodriguez, A. & Laio, A. Clustering by fast search and
   find of density peaks. Science 344, 1492–1496 (2014).
====================================================================
"""
from copy import deepcopy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.size'] = 18


class FastCluster:
    def __init__(self, points, distant_func, dc=None):
        """Implement Algorithm demonstrated on [1].

        [1]. Rodriguez, A. & Laio, A. Clustering by fast search and
        find of density peaks. Science 344, 1492–1496 (2014).
        """
        # distant_func 的输入是 point1，point2
        self.distant_func = distant_func
        self.dc = dc
        self.points = points

        self._distant_matrix(points)
        if self.dc is None:
            self.dc = self._default_dc()

        self._local_density()

        # 重要中间结果
        self.centers = None
        self.clusters = None

    def _default_dc(self):
        dist = deepcopy(self.dist_matrix)
        dist = dist.reshape(-1)
        dist.sort()
        return round(dist[int(len(dist) * 0.02)], 4)

    def _distant_matrix(self, points):
        """计算全部样本的距离矩阵

        :param points: list of sample
            样本点
        :return:
        """
        self.total_number = total_number = len(points)
        dist = np.zeros((total_number, total_number))

        for i in range(total_number):
            for j in range(i+1, total_number):
                d = self.distant_func(points[i], points[j])
                dist[i][j] = d
                dist[j][i] = d
        self.dist_matrix = dist

    def _local_density(self):
        if self.dist_matrix is None:
            raise ValueError('distant matrix is None')

        total_number = self.total_number

        # 计算局部密度
        ld = np.zeros(total_number)
        for i in range(total_number):
            ld[i] = np.sum(np.exp(-(self.dist_matrix[i]/self.dc)**2))
            # row = self.dist_matrix[i]
            # ld[i] = np.sum(row <= self.dc)
        self.ld = ld

        # 计算最小距离
        md = np.zeros(total_number)
        for i in range(total_number):
            row = self.dist_matrix[i][ld > ld[i]]
            if len(row) > 0:
                md[i] = np.min(row)
            else:
                md[i] = np.max(self.dist_matrix[i])
        self.md = md
        self.gamma = ld * md

    def plot_decision_graph(self):
        fig = plt.figure(figsize=(16, 9))
        ax = fig.subplots(1, 1)
        y = sorted(self.gamma, reverse=True)
        x = list(range(len(y)))
        ax.scatter(x, y)
        plt.xlabel('n'), plt.ylabel('gamma')
        plt.title("decision graph of fast cluster")

    def _nearest_neighbor(self, clusters, index):
        dist_matrix = self.dist_matrix
        ld = self.ld
        dd = 10000000
        neighbor = -1.0
        for i in range(self.total_number):
            if dist_matrix[index, i] < dd and ld[index] < ld[i]:
                dd = dist_matrix[index, i]
                neighbor = i
        if clusters[neighbor] == -1.0:
            clusters[neighbor] = self._nearest_neighbor(clusters, neighbor)
        return clusters[neighbor]

    def fit(self, rate):
        gamma = self.gamma
        threshold = rate * np.max(gamma)
        # 找出类簇中心
        clusters = -1 * np.ones(self.total_number, dtype=np.int)
        center = 0
        for i in range(self.total_number):
            if gamma[i] > threshold:
                clusters[i] = center
                center += 1

        for i in range(self.total_number):
            if clusters[i] == -1:
                clusters[i] = self._nearest_neighbor(clusters, i)

        self.clusters = clusters
        return clusters
