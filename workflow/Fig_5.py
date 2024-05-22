# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

########################################################## Maps #######################################################################################
## Total drought duration
path = '/path/to/plotting/folder/'
df = pd.read_csv(path + 'plot.csv', header=0)

gages = gpd.read_file(path + '32_gages.shp')
rivers = gpd.read_file(path + '7_rivers.shp')
reservoirs = gpd.read_file(path + 'TWDB_SWP2012_Major_Reservoirs_prj_huc2.shp')
huc2 = gpd.read_file(path + 'WBDHU2.shp')
texas = gpd.read_file(path + 'Texas.shp')
merged_data = gages.merge(df, on='CP_ID')

vmin = 1
vmax = 4
tick_interval = 1
ticks = np.arange(vmin, vmax + tick_interval, tick_interval)

fig, ax = plt.subplots(figsize=(10, 8))
rivers.plot(ax=ax, color='dodgerblue', alpha=1, zorder=1)
texas.plot(ax=ax, facecolor='none', alpha=0.5, edgecolor='grey', linewidth=1, zorder=2)
huc2.plot(ax=ax, facecolor='none', edgecolor='grey', linewidth=1.5, zorder=3)
reservoirs.plot(ax=ax, color='grey', edgecolor='grey', zorder=4)

vmin = -150
vmax = 150
merged_data['relative_change_total_duration'] *= 100
merged_data_plot = merged_data.plot(ax=ax, alpha=1, column='relative_change_total_duration', markersize=100, edgecolor='grey', zorder=5, vmin=vmin, vmax=vmax, cmap='bwr')
scalar_mappable = plt.cm.ScalarMappable(cmap='bwr') 
scalar_mappable.set_array([])  

# Set the minimum and maximum values of the colormap
scalar_mappable.set_clim(vmin=vmin, vmax=vmax)
tick_interval = 50
ticks = np.arange(vmin, vmax + tick_interval, tick_interval)
# Add a colorbar with smaller size inside the figure frame
cbar = plt.colorbar(scalar_mappable, ax=ax, orientation='horizontal', label='Relative change (%)', pad=-0.2, shrink=0.5, extend='both', ticks=ticks) #, pad=-0.2,shrink = 0.5 , ticks=np.linspace(-50, 50,21)
cbar.ax.xaxis.set_ticks_position('top')  # Move ticks to the top
cbar.ax.xaxis.set_label_position('top')  # Move label to the top
cbar.ax.tick_params(labelsize=10)  # Adjust tick label size
cbar.ax.set_xlabel('Relative change (%)', fontsize=12,labelpad=15)  # Adjust label size

# Specify the location of the colorbar
cbar.ax.set_position([0.1, 0.15, 0.5, 0.02])  # [left, bottom, width, height]

ax.text(0.02, 0.92, '(c)', transform=ax.transAxes, fontsize=17)
ax.tick_params(axis='both', which='both', length=0)
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.text(0.49, 0.3, 'Nueces R.', transform=ax.transAxes, fontsize=8,rotation = -75, color='dodgerblue')
ax.text(0.61, 0.29, 'San Antonio R.', transform=ax.transAxes, fontsize=8,rotation = -33, color='dodgerblue')
ax.text(0.41, 0.58, 'Colorado R.', transform=ax.transAxes, fontsize=8,rotation = -40, color='dodgerblue')
ax.text(0.6, 0.53, 'Brazos R.', transform=ax.transAxes, fontsize=8,rotation = -58, color='dodgerblue')
ax.text(0.75, 0.45, 'Trinity R.', transform=ax.transAxes, fontsize=8,rotation = -33, color='dodgerblue')
ax.text(0.8, 0.505, 'Neches R.', transform=ax.transAxes, fontsize=8,rotation = -40, color='dodgerblue')
ax.text(0.75, 0.60, 'Sabine R.', transform=ax.transAxes, fontsize=8,rotation = -24, color='dodgerblue')
plt.savefig(path + 'total_time_drought_change.png',dpi=600,bbox_inches='tight')

## Total drought severity

fig, ax = plt.subplots(figsize=(10, 8))
rivers.plot(ax=ax, color='dodgerblue', alpha=1, zorder=1)
texas.plot(ax=ax, facecolor='none', alpha=0.5, edgecolor='grey', linewidth=1, zorder=2)
huc2.plot(ax=ax, facecolor='none', edgecolor='grey', linewidth=1.5, zorder=3)
reservoirs.plot(ax=ax, color='grey', edgecolor='grey', zorder=4)

vmin = -100
vmax = 100
merged_data['relative_change_total_severity'] *= 100
merged_data_plot = merged_data.plot(ax=ax, alpha=1, column='relative_change_total_severity', markersize=100, edgecolor='grey', zorder=5, vmin=vmin, vmax=vmax, cmap='bwr')

scalar_mappable = plt.cm.ScalarMappable(cmap='bwr') 
scalar_mappable.set_array([])  

# Set the minimum and maximum values of the colormap
scalar_mappable.set_clim(vmin=vmin, vmax=vmax)
tick_interval = 50
ticks = np.arange(vmin, vmax + tick_interval, tick_interval)
# Add a colorbar with smaller size inside the figure frame
cbar = plt.colorbar(scalar_mappable, ax=ax, orientation='horizontal', label='Relative change (%)', pad=-0.2, shrink=0.5, extend='both', ticks=ticks) #, pad=-0.2,shrink = 0.5 , ticks=np.linspace(-50, 50,21)
cbar.ax.xaxis.set_ticks_position('top')  # Move ticks to the top
cbar.ax.xaxis.set_label_position('top')  # Move label to the top
cbar.ax.tick_params(labelsize=10)  # Adjust tick label size
cbar.ax.set_xlabel('Relative change (%)', fontsize=12,labelpad=15)  # Adjust label size

# Specify the location of the colorbar
cbar.ax.set_position([0.1, 0.15, 0.5, 0.02])  # [left, bottom, width, height]

ax.text(0.02, 0.92, '(c)', transform=ax.transAxes, fontsize=17)
ax.tick_params(axis='both', which='both', length=0)
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.text(0.49, 0.3, 'Nueces R.', transform=ax.transAxes, fontsize=8,rotation = -75, color='dodgerblue')
ax.text(0.61, 0.29, 'San Antonio R.', transform=ax.transAxes, fontsize=8,rotation = -33, color='dodgerblue')
ax.text(0.41, 0.58, 'Colorado R.', transform=ax.transAxes, fontsize=8,rotation = -40, color='dodgerblue')
ax.text(0.6, 0.53, 'Brazos R.', transform=ax.transAxes, fontsize=8,rotation = -58, color='dodgerblue')
ax.text(0.75, 0.45, 'Trinity R.', transform=ax.transAxes, fontsize=8,rotation = -33, color='dodgerblue')
ax.text(0.8, 0.505, 'Neches R.', transform=ax.transAxes, fontsize=8,rotation = -40, color='dodgerblue')
ax.text(0.75, 0.60, 'Sabine R.', transform=ax.transAxes, fontsize=8,rotation = -24, color='dodgerblue')
plt.savefig(path + 'total_severity_drought_change.png',dpi=600,bbox_inches='tight')

########################################################## Boxplots #######################################################################################

## Total drought duration

data = pd.read_csv(path + 'plot.csv', header=0)
fig, ax1 = plt.subplots()

positions = [1, 2]
boxprops = dict(color='green',linewidth=1)  # Set the color of the box to black
medianprops = dict(color='green', linewidth=2) # Set the color of the median line to black
whiskerprops = dict(color='green', linewidth=1)  # Set the color of the whiskers to black
flierprops = dict(marker='o', markerfacecolor='none', markersize=5, linestyle='none', markeredgecolor='green')  # Set the style of the outliers
data[[ 'total duration per year_nat','total duration per year_gaged']].boxplot(ax=ax1, positions=positions, patch_artist=False, boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, flierprops=flierprops, widths=0.6, showfliers=True)  # Adjust the widths as neededax1.set_ylabel('Response time (month)')
plt.grid(False)
for whisker in ax1.lines[1:100]:
    whisker.set_color('green')
# Creating a secondary y-axis for the third column (relative change)
ax2 = ax1.twinx()
boxprops = dict(color='orange')  # Set the color of the box to black
medianprops = dict(color='orange', linewidth=2) # Set the color of the median line to black
whiskerprops = dict(color='orange')  # Set the color of the whiskers to black
flierprops = dict(marker='o', markerfacecolor='none', markersize=5, linestyle='none', markeredgecolor='orange')  # Set the style of the outliers
ax2.boxplot(data['relative_change_total_duration']*100, positions=[3], patch_artist=False, boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, widths=0.6,flierprops=flierprops)  # Adjust the widths as needed

ax1.set_ylim(top=7)
ax2.set_ylim(bottom = -100, top=100)
ax1.set_xticks([1, 2, 3])
ax1.set_xticklabels(['Natural Q','Regulated Q', 'Relative change'], rotation=0, fontsize = 14)
ax1.set_ylabel('Average drought duration per year\n(months)', fontsize = 15,labelpad=10)

ax2.set_ylabel('Relative change (%)', fontsize = 15,labelpad=10)
# Increase the size of y tick fontsize
ax1.tick_params(axis='y', labelsize=15)
ax2.tick_params(axis='y', labelsize=15) #,colors='orange
# Set the color of the percentile lines for the third box to orange
for whisker in ax2.lines[2:8]:
    whisker.set_color('orange')

plt.grid(False)
ax1.text(0.1, 0.88, '(c)', transform=ax1.transAxes, fontsize=17) # , fontweight='bold', va='top'
plt.tight_layout()
plt.savefig(path + 'total_time_drought_box.png',dpi=600,bbox_inches='tight')


## Total drought severity


fig, ax1 = plt.subplots()
positions = [1, 2]
boxprops = dict(color='green',linewidth=1)  # Set the color of the box to black
medianprops = dict(color='green', linewidth=2) # Set the color of the median line to black
whiskerprops = dict(color='green', linewidth=1)  # Set the color of the whiskers to black
flierprops = dict(marker='o', markerfacecolor='none', markersize=5, linestyle='none', markeredgecolor='green')  # Set the style of the outliers
data[[ 'total severity per year_nat','total severity per year_gaged']].boxplot(ax=ax1, positions=positions, patch_artist=False, boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, flierprops=flierprops, widths=0.6, showfliers=True)  # Adjust the widths as neededax1.set_ylabel('Response time (month)')
plt.grid(False)
for whisker in ax1.lines[1:100]:
    whisker.set_color('green')
# Creating a secondary y-axis for the third column (relative change)
ax2 = ax1.twinx()
boxprops = dict(color='orange')  # Set the color of the box to black
medianprops = dict(color='orange', linewidth=2) # Set the color of the median line to black
whiskerprops = dict(color='orange')  # Set the color of the whiskers to black
flierprops = dict(marker='o', markerfacecolor='none', markersize=5, linestyle='none', markeredgecolor='orange')  # Set the style of the outliers
ax2.boxplot(data['relative_change_total_severity']*100, positions=[3], patch_artist=False, boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, widths=0.6,flierprops=flierprops)  # Adjust the widths as needed

ax1.set_ylim(top=14)
ax2.set_ylim(top=300)

ax1.set_xticks([1, 2, 3])
ax1.set_xticklabels(['Natural Q','Regulated Q', 'Relative change'], rotation=0, fontsize = 14)
ax1.set_ylabel('Average drought severity per year', fontsize = 15,labelpad=10)

ax2.set_ylabel('Relative change (%)', fontsize = 15,labelpad=10)
# Increase the size of y tick fontsize
ax1.tick_params(axis='y', labelsize=15)
ax2.tick_params(axis='y', labelsize=15) #,colors='orange
# Set the color of the percentile lines for the third box to orange
for whisker in ax2.lines[2:8]:
    whisker.set_color('orange')

plt.grid(False)
ax1.text(0.1, 0.88, '(d)', transform=ax1.transAxes, fontsize=17) # , fontweight='bold', va='top'
plt.tight_layout()
plt.savefig(path + 'total_severity_drought_box.png',dpi=600,bbox_inches='tight')