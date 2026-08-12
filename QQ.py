

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


import numpy as np
from scipy import stats


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


df1 = pd.read_csv("./G2RT.csv")


for column in df1.columns:

    data = df1[column]
    
    # Q-Q plot
    plt.figure(figsize=(8, 6))
    stats.probplot(df1[column], dist="norm", plot=plt)
    plt.title(f'Q-Q plot for RIGHT STEM - GROUP2 - {column}')
    plt.show()
