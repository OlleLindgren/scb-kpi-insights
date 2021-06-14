from reader import values, weights, diff

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

def correlate(df1: pd.DataFrame, df2: pd.DataFrame) -> float:
    
    _ix = df1.dropna(axis=0).dropna(axis=1).index.intersection(df2.index)
    _cols = df1.dropna(axis=0).dropna(axis=1).columns.intersection(df2.columns)

    _df1 = df1.loc[_ix, _cols]
    _df2 = df2.loc[_ix, _cols]

    return np.corrcoef(_df1.values.ravel(), _df2.values.ravel())[0,1]

rel_weights = weights.dropna()/weights.sum()
rel_values = values.dropna()/values.sum()

print(f'(d weight, d value)     correlation is {correlate(diff(rel_weights), diff(rel_values)):.2f}')
print(f'(weight, d value)       correlation is {correlate(rel_weights, diff(rel_values)):.2f}')
print(f'(d weight, d log value) correlation is {correlate(diff(rel_weights), diff(rel_values.apply(np.log))):.2f}')
print(f'(weight, d log value)   correlation is {correlate(rel_weights, diff(rel_values.apply(np.log))):.2f}')

plt.show()
