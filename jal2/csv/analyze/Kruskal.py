import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kruskal
from scipy.stats import shapiro

from tabulate import tabulate

def display_dict_as_table(data):
    # Convert dictionary to a list of tuples (key, value)
    table = [(key, value) for key, value in data.items()]
    # Use tabulate to format it as a table
    print(tabulate(table, headers=["Key", "Value"], tablefmt="grid"))



# Constants
FILE_NAME = "BSC"
GROUPS = {1: "Healthy", 2: "Sham-pre", 3: "Treat-pre", 4: "Sham-post", 5: "Treat-post", 6: "Migrainure"}
ALPHA = 0.05  # Significance level


# Load data
dfx = pd.read_csv(f'./{FILE_NAME}.csv')

try:
    del dfx["subNO"]
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

resultmap = {}

for side in ["RT", "LT"]:
    for key in namemap.keys():
        
        # Extract relevant columns and filter data
        data_dict = {
            'pre-treatment': dfx.loc[dfx['group'] == 3, side + key],  # Treat-pre
            'pre-simulation': dfx.loc[dfx['group'] == 2, side + key],  # Sham-pre
            'post-treatment': dfx.loc[dfx['group'] == 5, side + key],  # Treat-post
            'post-simulation': dfx.loc[dfx['group'] == 4, side + key],  # Sham-post
        }
        
        # Debug: Print data for each group
        print("\nData for each group:")
        for group_name, values in data_dict.items():
            print(f"{group_name}: {values}")
        
        # Convert dictionary to DataFrame
        df = pd.DataFrame(data_dict)
        
        # Reshape data into long format
        df = df.melt(var_name='Group', value_name='Value')
        
        # Debug: Check for missing or identical values
        print("\nChecking data for issues...")
        for group_name, group_data in df.groupby('Group'):
            print(f"Group: {group_name}, Data: {group_data['Value'].values}")
            if group_data['Value'].isna().all():
                print(f"  --> Group '{group_name}' has no valid data!")
            elif len(set(group_data['Value'])) == 1:
                print(f"  --> Group '{group_name}' has identical values: {group_data['Value'].values}")
        
        # Perform Kruskal-Wallis Test
        # print("\nPerforming Kruskal-Wallis Test...")
        groups = [group['Value'].dropna().values for name, group in df.groupby('Group')]
        if len(groups) < 2:
            print("Error: Not enough groups with valid data for Kruskal-Wallis test.")
        else:
            stat, p_value = kruskal(*groups)
        
            # Print results
            # print(f"\nKruskal-Wallis Test Results:")
            # print(f"Test Statistic: {stat:.4f}, p-value: {p_value:.4f}" if p_value is not None else "Invalid test (NaN).")
        
            # Conclusion
            if p_value < ALPHA:
                print(f"\nConclusion: There is a significant difference between the groups (p-value = {p_value:.4f}).")
            else:
                print(f"\nConclusion: There is no significant difference between the groups (p-value = {p_value:.4f}).")
        
        sidename = ["Left"]
        if(side == "RT"):
           sidename[0] = "Right"
       
        resultmap[sidename[0]+" "+ namemap[key]] = p_value
        
        # # Visualize distributions
        # sns.boxplot(data=df, x='Group', y='Value')
        # plt.title("Group Value Distributions")
        # plt.xticks(rotation=45)
        # plt.show()


print(display_dict_as_table(resultmap))
    

