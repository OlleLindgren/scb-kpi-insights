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

values = _read_csv(os.path.join(DATA_DIR, 'values.csv'))
weights = _read_csv(os.path.join(DATA_DIR, 'weights.csv'))

diffs = (values - values.shift(1, axis=1)).drop(columns=values.columns[0])
log_diffs = (values.apply(np.log) - values.shift(1, axis=1).apply(np.log)).drop(columns=values.columns[0])

weighted_diffs = diffs.multiply(weights)[weights.columns.intersection(diffs.columns)]
weighted_log_diffs = log_diffs.multiply(weights)[weights.columns.intersection(diffs.columns)]
