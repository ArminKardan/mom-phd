
import numpy as np
from scipy import stats


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

df1 = pd.read_csv("./G2LT.csv")
# df2 = pd.read_csv("./G2LT.csv")

for column in df1.columns:

    data = df1[column]
    
    result = stats.anderson(data, dist='norm')
    print(f"Statistic: {result.statistic}")
    print(f"Critical Values: {result.critical_values}")
    print(f"Significance Levels: {result.significance_level}")