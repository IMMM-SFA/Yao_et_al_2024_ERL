# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



## Relative change in monthly cumulative occurrence

file_path = '/path/to/plotting/folder/Relative_change_frequncy_monthly.csv' 
df = pd.read_csv(file_path)
df_melted = df.melt(id_vars=["CP_ID", "gage"], value_vars=['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec','Jan', 'Feb'],
                    var_name='Month', value_name='Value')

plt.figure(figsize=(12, 6))
flierprops = dict(marker='o', markerfacecolor='none', markersize=5, linestyle='none') #, markeredgecolor='orange' 
boxprops = dict(facecolor='none')
ax = sns.boxplot(x='Month', y='Value', data=df_melted, palette='Set3', flierprops=flierprops, boxprops=boxprops)
seasons = {
    'Spring': {'months': ['Mar', 'Apr', 'May'], 'color': 'lightgreen'},
    'Summer': {'months': ['Jun', 'Jul', 'Aug'], 'color': 'lightyellow'},
    'Autumn': {'months': ['Sep', 'Oct', 'Nov'], 'color': 'lightcoral'},
    'Winter': {'months': ['Dec', 'Jan', 'Feb'], 'color': 'lightblue'}
}

month_positions = {month: pos for pos, month in enumerate([ 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec','Jan', 'Feb'])}
for season, info in seasons.items():
    months = info['months']
    color = info['color']
    start_pos = month_positions[months[0]] - 0.5
    end_pos = month_positions[months[-1]] + 0.5
    ax.axvspan(start_pos, end_pos, facecolor=color, alpha=0.3)
    
plt.title('Relative change in monthly cumulative occurence',fontsize=19)

plt.xlabel('')
plt.ylabel('%', fontsize=19)
plt.xticks(rotation=0 ,fontsize=19)
plt.yticks(fontsize=17)
plt.axhline(y = 0, color = 'orangered', linestyle = 'dotted',linewidth=3) # 
plt.ylim(-120,350)
plt.tight_layout()
plt.savefig('/path/to/plotting/folder/Relative_change_occurrence_monthly.png',dpi=600,bbox_inches='tight')




## Relative change in monthly cumulative severity

file_path = '/path/to/plotting/folder/Relative_change_severity_monthly.csv' 
df = pd.read_csv(file_path)
df_melted = df.melt(id_vars=["CP_ID", "gage"], value_vars=['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec','Jan', 'Feb'],
                    var_name='Month', value_name='Value')

plt.figure(figsize=(12, 6))
flierprops = dict(marker='o', markerfacecolor='none', markersize=5, linestyle='none') #, markeredgecolor='orange' 
boxprops = dict(facecolor='none')
ax = sns.boxplot(x='Month', y='Value', data=df_melted, palette='Set3', flierprops=flierprops, boxprops=boxprops)

seasons = {
    'Spring': {'months': ['Mar', 'Apr', 'May'], 'color': 'lightgreen'},
    'Summer': {'months': ['Jun', 'Jul', 'Aug'], 'color': 'lightyellow'},
    'Autumn': {'months': ['Sep', 'Oct', 'Nov'], 'color': 'lightcoral'},
    'Winter': {'months': ['Dec', 'Jan', 'Feb'], 'color': 'lightblue'}
}

month_positions = {month: pos for pos, month in enumerate([ 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec','Jan', 'Feb'])}
for season, info in seasons.items():
    months = info['months']
    color = info['color']
    start_pos = month_positions[months[0]] - 0.5
    end_pos = month_positions[months[-1]] + 0.5
    ax.axvspan(start_pos, end_pos, facecolor=color, alpha=0.3)
plt.title('Relative change in monthly cumulative severity',fontsize=19)
plt.xlabel('')
plt.ylabel('%',fontsize=19)
plt.xticks(rotation=0 ,fontsize=19)
plt.yticks(fontsize=17)
plt.ylim(-120,350)
plt.axhline(y = 0, color = 'orangered', linestyle = 'dotted',linewidth=3) # 
plt.tight_layout()
plt.savefig('/path/to/plotting/folder/Relative_change_severity_monthly.png',dpi=600,bbox_inches='tight')




## Relative change in monthly Q10
file_path = '/path/to/plotting/folder/Relative_change_Q10_monthly.csv' 
df = pd.read_csv(file_path)
df_melted = df.melt(id_vars=["CP_ID", "gage"], value_vars=['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec','Jan', 'Feb'],
                    var_name='Month', value_name='Value')

plt.figure(figsize=(12, 6))
flierprops = dict(marker='o', markerfacecolor='none', markersize=5, linestyle='none') #, markeredgecolor='orange' 
boxprops = dict(facecolor='none')
ax = sns.boxplot(x='Month', y='Value', data=df_melted, palette='Set3', flierprops=flierprops, boxprops=boxprops)

seasons = {
    'Spring': {'months': ['Mar', 'Apr', 'May'], 'color': 'lightgreen'},
    'Summer': {'months': ['Jun', 'Jul', 'Aug'], 'color': 'lightyellow'},
    'Autumn': {'months': ['Sep', 'Oct', 'Nov'], 'color': 'lightcoral'},
    'Winter': {'months': ['Dec', 'Jan', 'Feb'], 'color': 'lightblue'}
}

month_positions = {month: pos for pos, month in enumerate([ 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec','Jan', 'Feb'])}
for season, info in seasons.items():
    months = info['months']
    color = info['color']
    start_pos = month_positions[months[0]] - 0.5
    end_pos = month_positions[months[-1]] + 0.5
    ax.axvspan(start_pos, end_pos, facecolor=color, alpha=0.3)
# Customize the plot
plt.title('Relative change in monthly Q$_{10}$',fontsize=19)
plt.xlabel('')
plt.ylabel('%',fontsize=19) 
plt.xticks(rotation=0 ,fontsize=19)
plt.yticks(fontsize=17)
plt.ylim(-150,1000)
plt.axhline(y = 0, color = 'orangered', linestyle = 'dotted',linewidth=3) # 
plt.tight_layout()
plt.savefig('/path/to/plotting/folder/Relative_change_Q10_monthly.png',dpi=600,bbox_inches='tight')