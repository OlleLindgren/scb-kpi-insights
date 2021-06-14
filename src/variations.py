from reader import values, weights, diff

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

def std(df: pd.DataFrame) -> pd.Series:
    # Row standard deviations
    return pd.DataFrame(data=zip(*df.replace(np.nan, 0).values), columns=df.index).std()

print(std(values.multiply(weights)).sort_values())