import numpy as np 
import pandas as pd 
import os

from settings import DATA_DIR


with open(os.path.join(DATA_DIR, 'years-items-values.csv'), 'rb') as f:
    for i, line in enumerate(f.readlines()):
        if i < 3:
            continue
        if i == 3:
            print(line)
        if i > 3:
            break

values = pd.read_csv(os.path.join(DATA_DIR, 'years-items-values.csv'), delimiter=',')
weights = pd.read_csv(os.path.join(DATA_DIR, 'years-items-weights.csv'), delimiter=',')

print(values)
print(weights)