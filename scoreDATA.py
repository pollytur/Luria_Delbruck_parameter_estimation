from generateLD import *


def score(data, m, single=True, d=None):
    '''
    :param data:
    :param m:
    :param single:
    :param d:
    :return:
    '''
    mx = max(data) + 1
    tabdata = [0 for _ in range(mx)]
    for element in data:
        tabdata[element] += 1
    if single:
        dist = generateLD(m, mx)
    else:
        dist = generate_two_params(m, d, mx)
    score = sum(-np.log(np.array(dist) ** tabdata))
    return score

# data = [0, 65, 9, 2, 16, 4, 3]
# m= 6

# print(score(data, m))