# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('axes', facecolor='#6E838A')
mpl.rc('axes', edgecolor='#737373')

# datas in
datas = pd.read_csv('*.csv', encoding='gbk')


class stacked_bar_plot:
    def __init__(self, datas):
        self.version = '1.0'
        self.datas = datas

    def parse_datas(datas=datas):
        d_values = datas.iloc[:, 2].values.reshape((24, 3))
        x_labels = datas.iloc[:, 0].unique()
        legends = datas.iloc[:, 1].unique()
        return d_values, x_labels, legends

    d_values, x_labels, legends = parse_datas(datas)

    # 重整数据
    def compute_ratio(x):
        """
        计算每一类数据的占比
        """
        sum_ = sum(x)
        ratios = []
        for i in x:
            ratio = i / sum_
            ratios.append(ratio)
        return ratios

    per_ratio = np.apply_along_axis(compute_ratio, 1, d_values)

    def stacked_bar(self, width=0.6):
        per_ratio = self.per_ratio * 50
        # split into three 
        gcq_ratio = per_ratio[:, 0]
        lwq_ratio = per_ratio[:, 2]
        other_ratio = per_ratio[:, 1]
        # set bar left edge
        ind = np.arange(24)

        plt.figure(figsize=(20, 7), facecolor='#6E838A')
        plt.ylim(0, 55)
        plt.bar(ind + 0.5, gcq_ratio, width, color='#588fc1')
        plt.bar(ind + 0.5, lwq_ratio, width, bottom=gcq_ratio, color='#6a9f46')
        plt.bar(ind + 0.5, other_ratio, width, bottom=gcq_ratio + lwq_ratio, color='#e7af08')

        # add x,y ticks
        xy_font = mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\STKAITI.TTF', size=18)
        x_labels = datas.utility.unique()
        plt.xticks(ind + 0.8, x_labels, fontproperties=xy_font, rotation=90)
        plt.yticks(np.arange(0, 50, 5), np.arange(0, 100, 10), fontproperties=xy_font)

        # add legend
        l_font = mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\STKAITI.TTF', size=16)
        plt.legend(('*', '*', '*'), prop=l_font,
                   ncol=3, frameon=False, loc='upper center')

        for label in plt.axes().get_xticklabels() + plt.axes().get_yticklabels():
            label.set_color('white')

        # add title
        t_font = mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\STKAITI.TTF', size=28)
        plt.title('*', fontproperties=t_font, color='white')

        # add x label
        plt.ylabel('*', fontproperties=xy_font, color='white')
        plt.show()
