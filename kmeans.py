#%%
import pandas as pd
import pyreadstat

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv("./G1RT.csv")
df2 = pd.read_csv("./G2RT.csv")

# print(df2)

df1["group"] = 1
df2["group"] = 2


df = pd.concat([df1, df2])

dfn = df.drop(columns=['group']) 


scaler = StandardScaler()
scaled_data = scaler.fit_transform(dfn)

kmeans = KMeans(n_clusters=2, random_state=42)  

df['cluster'] = kmeans.fit_predict(scaled_data)


print(df)

print()
print()






from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, accuracy_score
from scipy.optimize import linear_sum_assignment
import pandas as pd
import numpy as np

# Example: Restoring group and cluster column
# df = your dataframe with 'group' and 'cluster'

# Mapping clusters to groups using a confusion matrix
confusion_matrix = pd.crosstab(df['cluster'], df['group'])

# Hungarian algorithm to maximize mapping
row_ind, col_ind = linear_sum_assignment(-confusion_matrix.values)
mapping = {row: col_ind[i] for i, row in enumerate(row_ind)}

# Map clusters to groups
df['mapped_cluster'] = df['cluster'].map(mapping)

# Metrics
ari = adjusted_rand_score(df['group'], df['cluster'])
nmi = normalized_mutual_info_score(df['group'], df['cluster'])
accuracy = accuracy_score(df['group'], df['mapped_cluster'])

print("Adjusted Rand Index (ARI):", ari)
print("Normalized Mutual Information (NMI):", nmi)
print("Accuracy:", accuracy)

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix)















