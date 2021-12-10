from statistics import median

  
def MLE_step_m(m, dif, score_data, first=False, maximize=False):
  '''
  m is initial mutation rate estimation - float
  dif is presion of the current step - float
  score_data - function to estimate the m
  fisrt indicates if it is the first evaluation - Boolean
  maximize indicates if we need to modify scores - Boolean
  '''
  scores = [0 1 0]
  while scores[1] > min(scores):
    ms = [m - dif, m, m + dif]
    if first and not maximize:
      for i in range(len(ms)):
        if ms[i] < 0:
          ms[i] = 0
    scores = [score_data(data, ms[0])),
              score_data(data, ms[1]),
              score_data(data, ms[2])]
    if maximize:
      for i in range(len(scores)):
        if ms[i] < 0:
          scores[i] = max(scores) + 1
    m = ms[scores.index(min(scores))]
  return m


def MLE_step_d(d, dif, m):
  '''
  d is initial death rate estimation - float
  dif is presion of the current step - float
  m is the value of m - float
  '''
  scores = [0 1 0]
  while scores[1] > min(scores):
    ds = [d - dif, d, d + dif]
    scores = [score_data(data, m, ds[0])),
              score_data(data, m, ds[1]),
              score_data(data, m, ds[2])]
    if maximize:
      for i in range(len(scores)):
        if ds[i] < 0:
          scores[i] = max(scores) + 1
    d = ds[scores.index(min(scores))]
  return d
  
  
def find_mut_rate_only(data, score_data, dif=[1, 0.1, 0.01, 0.001], maximize=False):
  '''
  data is inpt data - list
  score_data - function to estimate the m
  dif is precisions of m - list
  maximize indicates if we need to modify scores - Boolean
  '''  
  # TODO - check why m is no more than 10 and why + 0.1 ???
  m = median(data) + 0.1
  if m > 10:
    m = 10
  first = True
  for i in dif:
    m = MLE_step(m, i, first, maximize)
    first = False
  return m


def find_mut_and_death_rate(data, score_data, 
                            dif_m=[1, 0.1, 0.01, 0.001],
                            dif_d=[1, 0.1, 0.01, 0.001]):
  '''
  data is inpt data - list
  score_data - function to estimate the m
  dif_m is precisions of m - list
  dif_d is precisions of d - list
  '''                  
  m = find_mut_rate_only(data, score_data, dif_m, maximize=True)
  for i in dif_d:
    d = MLE_step_d(d, i, m)
  return (m, d)