import generateLD
import scoreDATA
import MLE
import pandas as pd

df1 = pd.read_csv('mutantcount1', header=None)
data = df1.to_numpy().flatten()

