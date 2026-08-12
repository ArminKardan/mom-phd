import numpy as np
from scipy import stats


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats



df1 = pd.read_csv("./G2RT.csv")
# df2 = pd.read_csv("./G2LT.csv")

for column in df1.columns:

    data = df1[column]
    
    stat, p_value = stats.shapiro(data)
    print(f"RIGHT STEM GROUP2 - {column}:")
    print(f"Shapiro-Wilk test statistic: {stat}")
    print(f"P-value: {p_value}")
    
    if p_value > 0.05:
        print("Data looks like a normal distribution")
    else:
        print("Data does not look like a normal distribution")
    print()
    print()
