import numpy as np
import pandas as pd
from generateLD import generateLD

def score(data, m):
    mx = max(data)
    tabdata = [0 for _ in range(mx)]
    for i in range(mx):
        tabdata[i] = len(np.where(np.array(data) == i))

    dist = generateLD(m, mx)
    score = sum(-np.log(np.array(dist)**tabdata))

    return score
    
# df1 = pd.read_csv('mutantcount1', header=None)
# m = np.median(df1)
# data = df1.to_numpy().flatten()
# print(score(data, m))
