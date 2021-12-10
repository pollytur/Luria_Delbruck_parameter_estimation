from scoreDATA import score
from MLE import find_mut_rate_only
import pandas as pd

df1 = pd.read_csv('data/mutantcount1', header=None)
data = df1.to_numpy().flatten()

res = find_mut_rate_only(data, score, dif=[1, 0.1, 0.01, 0.001], maximize=False)
print(res)

