import pandas as pd
from collections import Counter
from zb.algorithms.fast_cluster import FastCluster
from fuzzywuzzy import fuzz

csv = r"C:\ZB\git_repo\tushare_gitlab\cninfo\data\pdf\SZ\000001.SZ\announcements_000001.csv"

texts = list(pd.read_csv(csv)['title'])


def distant_func(point1, point2):
    r = fuzz.ratio(point1, point2)
    return 1/(r+1)


fc = FastCluster(texts, distant_func=distant_func, dc=0.1)

fc.plot_decision_graph()
res = fc.fit(0.018)
# set(res)
c = Counter(res)

t_clusters = list(zip(texts, res))


