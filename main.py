from scoreDATA import score
from MLE import find_mut_rate_one_param, find_mut_and_death_rate
import pandas as pd
from functools import partial

if __name__ == "__main__":
    df1 = pd.read_csv('data/mutantcount1', header=None)
    data = df1.to_numpy().flatten()
    res = find_mut_rate_one_param(data, score, dif=[1, 0.1, 0.01, 0.001], Nc=200000)
    print(res)

    # TODO - add fitness
    # f = 0.9
    df2 = pd.read_csv('data/mutantcount2', header=None)
    data = df2.to_numpy().flatten()
    score_d_defined = partial(score, single=False, d=0.4)
    res = find_mut_rate_one_param(data, score_d_defined, dif=[1, 0.1, 0.01, 0.001], Nc=500000)
    print(res)

    df3 = pd.read_csv('data/mutantcount3', header=None)
    data = df3.to_numpy().flatten()
    # f = 0.8
    score_2_params = partial(score, single=False)
    res = find_mut_and_death_rate(data, score_2_params, Nc=1000000)
    print(res)
