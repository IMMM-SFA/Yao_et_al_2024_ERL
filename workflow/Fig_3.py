# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

########################################################## Fitting points ####################################################################################

fig, ax1 = plt.subplots()

data = pd.read_csv(path + 'plot.csv', header=0)
# Extract the columns
x = 100 * data['relative change_Q10']
y = 100 * data['pro rate relative change']

# Plot the scatter plot
plt.scatter(x, y, label='Data',color = 'orange',edgecolor='grey',s = 50)

# Calculate linear fit
slope, intercept = np.polyfit(x, y, 1)

# Add the linear fit line
x_range = np.linspace(x.min(), x.max(), 100)  # Generate x-values with equal intervals
plt.plot(x_range, slope * x_range + intercept, 'r--', label='Linear Fit',color = 'grey')

# Calculate R-squared
residuals = y - (slope * x + intercept)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)

# Add the equation and R-squared value
equation = f'y = {slope:.2f}x + {intercept:.2f}\nR$^2$ = {r_squared:.2f}'
plt.text(0.5, 0.85, equation, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=15)

# Add labels and legend
plt.ylabel('Relative change in \npropagation rate (%)', fontsize=15, labelpad=10)
plt.xlabel('Relative change in average monthly Q$_{10}$ (%)', fontsize=15, labelpad=10)

# Increase the number of ticks on x-axis and y-axis
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig(path + 'Change_prorage_vs_change_Q10_Linear.png',dpi=600,bbox_inches='tight')
