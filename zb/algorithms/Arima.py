# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from zb_CodeSet.DataSet.load_dataset import load_monthly_milk_production


# step1. 输入数据，查看数据
dta = load_monthly_milk_production()
dta.plot(figsize=(12, 8))

# step2. 视情况，进行差分运算(通常从1阶差分开始)
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)
diff1 = dta['MilkProduction'].diff(1)  # 差分运算
diff1.plot(ax=ax1)


# step3. 确定合适的p, q参数
diff = dta.diff(1)  # 我们已经知道要使用一阶差分的时间序列，之前判断差分的程序可以注释掉
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(diff, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(diff, lags=40, ax=ax2)

# 根据 AIC / BIC / HQIC判断
arma_mod20 = sm.tsa.ARMA(dta, (7, 0)).fit()
print(arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic)
arma_mod30 = sm.tsa.ARMA(dta, (0, 1)).fit()
print(arma_mod30.aic, arma_mod30.bic, arma_mod30.hqic)
arma_mod40 = sm.tsa.ARMA(dta, (7, 1)).fit()
print(arma_mod40.aic, arma_mod40.bic, arma_mod40.hqic)
arma_mod50 = sm.tsa.ARMA(dta, (8, 0)).fit()
print(arma_mod50.aic, arma_mod50.bic, arma_mod50.hqic)



