from generateLD import *


def score(data, m, single=True, d=None):
    '''
    :param data:
    :param m:
    :param single:
    :param d:
    :return:
    '''
    mx = max(data)
    tabdata = [0 for _ in range(mx)]
    for i in range(mx):
        tabdata[i] = len(np.where(np.array(data) == i))
    if single:
        dist = generateLD(m, mx)
    else:
        dist = generate_two_params(m, d, mx)
    score = sum(-np.log(np.array(dist) ** tabdata))

    return score
