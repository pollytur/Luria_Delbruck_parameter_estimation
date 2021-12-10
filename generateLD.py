import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generateLD(m, max):
    ldDist = [np.exp(-m)]
    for i in range(1, max):
        x = np.array([i for i in range(len(ldDist))])
        temp = m/len(x)*sum(ldDist/(len(x) - x + 1))
        ldDist.append(temp)
    return ldDist

df1 = pd.read_csv('mutantcount1', header=None)
max = df1[0].max()
distrib = generateLD(np.median(df1), max)

plt.plot(distrib)
plt.xlabel('number of mutant cells')
plt.ylabel('probability of event')
plt.title("graph of the Luria Delbruck distribution for the file mutantcount1")
plt.show()
