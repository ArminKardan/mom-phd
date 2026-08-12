

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


df1 = pd.read_csv("./G1RT.csv")
df2 = pd.read_csv("./G2RT.csv")


cors = []
for column in df1.columns:
    # cor = np.corrcoef(df1[column], df2[column])
    # print(f"Correlation {column}:", cor[0,1])
    # cors.append(cor[0,1])
    print(f"STDEV {column} G2:", round(np.std(df2[column]),2))
    # print(f"Mean {column} G2:", round(np.mean(df2[column]),2))


# import matplotlib.pyplot as plt
# plt.bar(df1.columns, cors, color='orange')
# plt.xlabel('Features')
# plt.ylabel('Correlations')
# plt.title('Cross Correlation between G1-A & G2 Features')
# plt.axhline(y=0.5, color='r', linestyle='--', label='Significance Threshold (0.5)')
# plt.legend()
# plt.show()