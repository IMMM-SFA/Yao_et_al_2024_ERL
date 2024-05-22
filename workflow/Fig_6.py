# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

path = '/path/to/plotting/folder/'
data = pd.read_csv(path + 'plot.csv', header=0)

x = 100 * data['relative change_Q10']
y = 100 * data['relative_change_total_duration']
# Plot the scatter plot
plt.scatter(x, y, label='Data',color = 'orange',edgecolor='grey',s = 50)

# Add labels and legend
plt.ylabel('Relative change in total\ndrought time (%)', fontsize=15, labelpad=10)
plt.xlabel('Regulation effects (%)', fontsize=15, labelpad=10)
plt.xlabel('Relative change in average monthly Q$_{10}$ (%)', fontsize=15, labelpad=10)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig(path + 'Change_total_drought_time_vs_Change_Q10.png',dpi=600,bbox_inches='tight')

## Total drought severity 

x = 100 * data['relative change_Q10']
y = 100 * data['relative_change_ave_severity']

# Plot the scatter plot
plt.scatter(x, y, label='Data', color='orange', edgecolor='grey', s=50)

# Add labels and legend
plt.ylabel('Relative change in average\ndrought severity (%)', fontsize=15, labelpad=10)
plt.xlabel('Regulation effects (%)', fontsize=15, labelpad=10)
plt.xlabel('Relative change in average monthly Q$_{10}$ (%)', fontsize=15, labelpad=10)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig(path + 'Change_ave_drought_severity_vs_Change_Q10_EXP.png',dpi=600,bbox_inches='tight')

