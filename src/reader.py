import numpy as np 
import pandas as pd 
import os

from settings import DATA_DIR

def _read_csv(filename):
    result = pd.read_csv(
        filename, 
        encoding='latin1', 
        index_col=0
    ).replace('..', np.nan)
    for col in result.columns:
        result[col] = result[col].astype(float)
    return result

def diff(df):
    return (df - df.shift(1, axis=1)).drop(columns=df.columns[0])

values = _read_csv(os.path.join(DATA_DIR, 'values.csv'))
weights = _read_csv(os.path.join(DATA_DIR, 'weights.csv'))
