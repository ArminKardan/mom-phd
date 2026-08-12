# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:44:39 2025

@author: Armin
"""

import pandas as pd
from scipy import stats

df1 = pd.read_csv("./G1RT.csv")
df2 = pd.read_csv("./G2RT.csv")





from scipy import stats

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

# Create a bar plot for the p-values
plt.bar(df1.columns, p_values, color='skyblue')
plt.xlabel('Features')
plt.ylabel('P-Value')
plt.title('T\P-Values from T-Test for Each Feature')
plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Threshold (0.05)')
plt.legend()
plt.show()

