import numpy as np
from math import factorial
from decimal import *


def generateLD(m, max):
    ldDist = [np.exp(-m)]
    for i in range(1, max):
        x = np.array([i for i in range(len(ldDist))])
        temp = m / len(x) * sum(ldDist / (len(x) - x + 1))
        ldDist.append(temp)
    return ldDist


def generate_poisson(lamb, max):
    lamb = Decimal(lamb)
    dist = [0] * (max)
    for i in range(max):
        with localcontext() as ctx:
            ctx.prec = 32
            if lamb != 0:
                inter = ctx.exp((-1) * lamb) * ctx.power(lamb, i)
            else:
                inter = 0
                # inter = Decimal('inf')
            dist[i] = float(inter / Decimal(factorial(i)))
    return dist


def generate_two_params(m, d, max):
    ld = np.asarray(generateLD(m, max))
    pois = np.asarray(generate_poisson(m * d, max))
    pois[np.isnan(pois)] = 0
    codist = []
    pois = pois.reshape(-1, 1)
    for i in range(max):
        mult = ld[: i + 1] @ np.fliplr(pois[:i + 1])
        codist.append(mult[0])
    return codist
