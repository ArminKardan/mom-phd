import os
import pandas as pd


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

file = "Z"
groups = {1:"Healthy", 2:"Sham-pre", 3:"Treat-pre", 4:"Sham-post", 5:"Treat-post", 6:"Migrainure"}
df = pd.read_csv(f'./{file}.csv')

columns = df.columns.tolist()

try:
    del df["subNO"]
except:
    pass

namemap = {
'supramarginalGyrus40':
'Supramarginal Gy BA 40',

'occiputLobMidTemporalGyrus37':
'MTGy BA 37',

'insula13':
'Insula BA 13',

'visualAssoAreaInfTemporalGyrus19':
'IT Gy BA 19',

'dorsalACC32':
'dorsal ACC BA 32',

'cerebellarPosteiorLobSemiLunar':
'Cerebellum Post Lob',

'dlPFCsupFrontalGyrus9':
'dlPFC  (SF Gy)BA 9',

'secondVisualCortexInfOccipitalGyrus18':
'Sec Visual C (ÌO Gy) BA 18',

'BrocaOperculumInfFrontalGyrus44':
'Broca O (IF Gy) BA 44',

'PreSuplimentoryMotor6':
'pre Supli MC BA 6',

'caudate':
'Caudate',

'supParietalLobule7':
'SPL BA 7',

'BrocaTriangleInfFrontalGyrus45':
'Broca T (IF Gy) BA 44',

'cerebellarTonsil':
'Cerebellum Tonsil',

'fusiform37':
'Fusiform BA 37',

'AntPFCmedFrontalGyrus10':
'ant PFC (MF Gy) BA 10',

'ventralPCC23':
'ventral PCC BA 23',

'cerebellarAntLobe':
'Cerebellum  Ant Lobe',

'angularGyrus39':
'Angular Gy BA 39',

'postcentralGyrus5':
'post central Gy BA 5',

'dorsalPCC31':
'dorsal PCC BA 31',

'ventralACC24':
'ventral ACC BA 24',

'thalamus':
'Thalamus',

'primarysomatosensorycortex1':
'S1 BA 1',


'cerebellarAntLobeCULMEN':
'Cerebellum Culmen',

}

namemap.keys()

def create_path(path):
    try:
        # Create the path if it doesn't exist
        os.makedirs(path, exist_ok=True)
        print(f"The path '{path}' was created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the path: {e}")
        

def DrawQQ(side, namekey, groupnum):
    # Q-Q plot
    gname = groups[groupnum]
    data = df.loc[df['group'] == groupnum, side+namekey]
    name = namemap[namekey]
    if side == "RT":
        name = "Right "+ name
    elif side == "LT":
        name = "Left "+ name
    plt.figure(figsize=(8, 6))
    stats.probplot(data, dist="norm", plot=plt)
    plt.title(f'Q-Q plot for {gname} - {name}')
    create_path(f"./{file}/QQ/QQ-{name}/")
    plt.savefig(f"./{file}/QQ/QQ-{name}/{groupnum}.png", format='png', dpi=300) 
    # plt.show()

for name in namemap.keys():
    for i in range(1,7):
        DrawQQ("RT",name, i)
        DrawQQ("LT",name, i)



