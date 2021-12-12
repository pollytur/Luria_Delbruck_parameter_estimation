import numpy as np
from math import factorial


def generateLD(m, max):
    ldDist = [np.exp(-m)]
    for i in range(1, max):
        x = np.array([i for i in range(len(ldDist))])
        temp = m / len(x) * sum(ldDist / (len(x) - x + 1))
        ldDist.append(temp)
    return ldDist


def generate_poisson(lamb, max):
    dist = [0] * (max + 1)
    for i in range(max + 1):
        dist[i] = (lamb ** i) * np.exp((-1) * lamb) / factorial(i)
    return dist


def generate_two_params(m, d, max):
    ld = np.asarray(generateLD(m, max))
    pois = np.asarray(generate_poisson(m * d, max))
    pois[np.isnan(pois)] = 0
    codist = []
    for i in range(max + 1):
        mult = ld[: i + 1] @ np.fliplr(pois[:i + 1])
        codist.append(mult)
    return codist
