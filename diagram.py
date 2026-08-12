
import pandas as pd
import pyreadstat

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


df1 = pd.read_csv("./G1RT.csv")
df2 = pd.read_csv("./G2RT.csv")


for column in df1.columns:
    t_stat, p_value = stats.ttest_ind(df1[column], df2[column])
    print(f"T-test for {column}:")
    print(f"  t-statistic: {t_stat}")
    print(f"  p-value: {p_value}")
    print("-" * 30)
    

import matplotlib.pyplot as plt
p_values = []
for column in df1.columns:
    t_stat, p_value = stats.ttest_ind(df1[column], df2[column])
    p_values.append(p_value)
plt.bar(df1.columns, p_values, color='skyblue')
plt.xlabel('Features')
plt.ylabel('P-Value')
plt.title('P-Values from T-Test for Each Feature')
plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Threshold (0.05)')
plt.legend()
plt.show()