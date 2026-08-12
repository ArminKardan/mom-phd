from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
import os
import pandas as pd




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
from tabulate import tabulate


file = "Z"
groups = {1:"Healthy", 2:"Sham-pre", 3:"Treat-pre", 4:"Sham-post", 5:"Treat-post", 6:"Migrainure"}
df = pd.read_csv(f'./{file}.csv')

columns = df.columns.tolist()


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

resultmap = {}

def create_path(path):
    try:
        # Create the path if it doesn't exist
        os.makedirs(path, exist_ok=True)
        print(f"The path '{path}' was created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the path: {e}")
        


def mann_whitney_u_test_with_plot(side, namekey, data1, data2, groupnum = "1-6", threshold=0.05):
    u_statistic, p_value = mannwhitneyu(data1, data2)
    
    gname = 'Healthy vs Migrainure'
    name = namemap[namekey]
    if side == "RT":
        name = "Right "+ name
    elif side == "LT":
        name = "Left "+ name
        
    # plt.figure(figsize=(6, 4))
    # plt.bar(['P-value', 'Threshold'], [p_value, threshold], color=['blue', 'red'])
    # plt.axhline(y=threshold, color='red', linestyle='--', label=f'Threshold ({threshold})')
    # plt.ylabel('Value')
    # plt.legend()
    
    # plt.title(f'Mann-Whitney-U P-value for {gname} \n {name}')
    # create_path(f"./{file}/Mann-Whitney-U/Mann-Whitney-U-{name}/")
    # plt.savefig(f"./{file}/Mann-Whitney-U/Mann-Whitney-U-{name}/{groupnum}.png", format='png', dpi=300) 

    
    sidename = ["Left"]
    if(side == "RT"):
        sidename[0] = "Right"
               
    resultmap[sidename[0]+" "+ namemap[namekey]] = p_value



def display_dict_as_table(data):
    # Convert dictionary to a list of tuples (key, value)
    table = [(key, value) for key, value in data.items()]
    # Use tabulate to format it as a table
    print(tabulate(table, headers=["Key", "Value"], tablefmt="grid"))




for namekey in namemap.keys():
    mann_whitney_u_test_with_plot("RT",namekey, df.loc[df['group'] == 1,"RT"+ namekey], df.loc[df['group'] == 6,"RT"+namekey])
    mann_whitney_u_test_with_plot("LT",namekey, df.loc[df['group'] == 1,"LT"+ namekey], df.loc[df['group'] == 6,"RT"+namekey])



print(display_dict_as_table(resultmap))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    