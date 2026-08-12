import pandas as pd
import pyreadstat

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

input_file = "RT Brainstem.sav"  # مسیر فایل sav

# df, meta = pyreadstat.read_sav(input_file)
df = pd.read_csv("./RT.csv")

df = df[["coppre", "voxelpre", "zpre","BSCpre", "group"]]

df[["group"]] = df[["group"]].applymap(lambda x: 1 if x == 1 else 2)

features_to_use = df.drop(columns=['group'])      




scaler = StandardScaler()
scaled_data = scaler.fit_transform(features_to_use)

kmeans = KMeans(n_clusters=2, random_state=42)  
df['Cluster'] = kmeans.fit_predict(scaled_data)


correlation_matrix = df.corr()

print(correlation_matrix)

df1 = df[df['group'] == 1]
df2 = df[df['group'] == 2]

from scipy import stats

for column in df.columns:
    t_stat, p_value = stats.ttest_ind(df1[column], df2[column])
    print(f"T-test for {column}:")
    print(f"  t-statistic: {t_stat}")
    print(f"  p-value: {p_value}")
    print("-" * 30)
    

print(df1.std())
print(df2.std())


import matplotlib.pyplot as plt

p_values = []

for column in df.columns:
    t_stat, p_value = stats.ttest_ind(df1[column], df2[column])
    p_values.append(p_value)

# Create a bar plot for the p-values
plt.bar(df.columns, p_values, color='skyblue')
plt.xlabel('Features')
plt.ylabel('T-Value')
plt.title('T-Values from T-Test for Each Feature')
plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Threshold (0.05)')
plt.legend()
plt.show()

# x = df["coppre"]
# y = df["voxelpre"]
# z = df["zpre"]

# colors = df["group"]

# # Create a 3D scatter plot
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')

# scatter = ax.scatter(x, y, z, c=colors, cmap='viridis', s=50)

# # Add labels
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# # Add a color bar
# cbar = plt.colorbar(scatter, ax=ax)
# cbar.set_label('Color Scale')

# # Show the plot
# plt.title("3D Scatter Plot")
# plt.show()






# cluster_0_group_1_count = 0
# cluster_1_group_2_count = 0

# for index, row in df.iterrows():
#     if row["Cluster"] == 0 and row["group"] == 1:
#         cluster_0_group_1_count = cluster_0_group_1_count + 1
#     else if row["Cluster"] == 0 and row["group"] == 2:
#         cluster_0_group_1_count = cluster_0_group_1_count + 1
    
print(df)


# ذخیره به فرمت CSV
# df.to_csv(output_file, index=False, encoding="utf-8")

