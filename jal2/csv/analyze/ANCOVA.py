import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import het_breuschpagan
from tabulate import tabulate
import pandas as pd
import numpy as np
from scipy.stats import f

# Constants
FILE_NAME = "COP"
GROUPS = {1: "Healthy", 2: "Sham-pre", 3: "Treat-pre", 4: "Sham-post", 5: "Treat-post", 6: "Migrainure"}
ALPHA = 0.05  # Significance level




def display_dict_as_table(data):
    # Convert dictionary to a list of tuples (key, value)
    table = [(key, value) for key, value in data.items()]
    # Use tabulate to format it as a table
    print(tabulate(table, headers=["Key", "Value"], tablefmt="grid"))


# Load data
dfx = pd.read_csv(f'./{FILE_NAME}.csv')


# dfx = pd.DataFrame({
#     "group":[3,3,3,3,5,5,5,5,  2,2,2,2,  4,4,4,4  ],
#     "RTdiet":[83,79,75,78,  79,77,72,74, 102,96,87,95, 97,93,85,93   ],
#     "LTdiet":[83,79,75,78,  79,77,72,74, 102,96,87,95, 97,93,85,93   ]
#     })

try:
    del dfx["subNO"]
except:
    pass

# namemap = {"diet":"DIET"}

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


for side in ["RT", "LT"]:
    
    for key in namemap.keys():
        data_dict = {
                    'pre-treatment': dfx.loc[dfx['group'] == 3, side + key],  # Treat-pre
                    'pre-simulation': dfx.loc[dfx['group'] == 2, side + key],  # Sham-pre
                    'post-treatment': dfx.loc[dfx['group'] == 5, side + key],  # Treat-post
                    'post-simulation': dfx.loc[dfx['group'] == 4, side + key],  # Sham-post
        }
        
        shampre = dfx.loc[dfx['group'] == 2,  side + key].tolist()
        shampost = dfx.loc[dfx['group'] == 4,  side + key].tolist()
        treatpre = dfx.loc[dfx['group'] == 3,  side + key].tolist()
        treatpost = dfx.loc[dfx['group'] == 5,  side + key].tolist()

        group = ['Sham' for i in shampost]+['Treat' for i in treatpre]
        pre = shampre + treatpre
        post = shampost + treatpost

        data = {
                'Group': group, 
                'Covariate': pre, #PRE
                'Dependent': post  #POST
            }


        df = pd.DataFrame(data)


        model = ols('Dependent ~ Group + Covariate', data=df).fit()

            # Perform ANOVA to get the p-value for the factor (Group)
        anova_table = sm.stats.anova_lm(model, typ=2)

        # print(anova_table)

        p_value = anova_table['PR(>F)']['Group']
        # print(f"\nP-value for the Group factor: {p_value:.4f}")


        sidename = ["Left"]
        if(side == "RT"):
           sidename[0] = "Right"
        resultmap[sidename[0]+" "+ namemap[key]] = p_value
        
        
print(display_dict_as_table(resultmap))        
        
        
        