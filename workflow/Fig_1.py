# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


path = '/path/to/plotting/folder/'
df = pd.read_csv(path + 'plot.csv', header=0)
gages = gpd.read_file(path + '32_gages.shp')
rivers = gpd.read_file(path + '7_rivers.shp')
reservoirs = gpd.read_file(path + 'TWDB_SWP2012_Major_Reservoirs_prj_huc2.shp')
huc2 = gpd.read_file(path + 'WBDHU2.shp')
texas = gpd.read_file(path + 'Texas.shp')
merged_data = gages.merge(df, on='CP_ID')

fig, ax = plt.subplots(figsize=(10, 8))
rivers.plot(ax=ax, color='dodgerblue', alpha=1, zorder=1)
texas.plot(ax=ax, facecolor='none', alpha=0.5, edgecolor='grey', linewidth=1, zorder=2)
huc2.plot(ax=ax, facecolor='none', edgecolor='grey', linewidth=1.5, zorder=3)
reservoirs.plot(ax=ax, color='grey', edgecolor='grey', zorder=4)
merged_data.plot(ax=ax, alpha=0.8, cmap='summer', column=merged_data['mean_annual_prec']*25.4, markersize=merged_data['number of year']*5, zorder=5) # summer_r cividis_r

# Define legend handles and labels
legend_handles1 = [plt.Line2D([0], [0], marker='o', markerfacecolor='None',  markeredgecolor='black',label='USGS streamgage', markersize=7, linestyle='None'),
                  plt.Line2D([0], [0], color='dodgerblue', lw=2, label='Major river'),
                  plt.Rectangle((0, 0), 1, 1, fc='grey', ec='grey', linewidth=1, label='Reservoir'), 
                  plt.Rectangle((0,0),1,1,fc="none", ec='grey', linewidth=1, label='Texas state',alpha = 0.5),
                  plt.Rectangle((0,0),1,1,fc="none", ec='grey', linewidth=1.5, label='Texas-Gulf basin')]

# Define the marker sizes 
marker_sizes = [30, 40, 50, 60,70,80]
marker_labels = ['30', '40', '50', '60','70','80']

# Create a legend for marker sizes
legend_handles2 = []
for size, label in zip(marker_sizes, marker_labels):
    legend_handles2.append(plt.scatter([], [], s=size*5, label=label, facecolor='None',edgecolor = 'black', alpha=0.5))
plt.legend(handles=legend_handles2, loc='lower left', title='Record length (years)', fontsize=12,title_fontsize=15, frameon=False)

# Show legend 1 in the upper right
legend1 = plt.legend(handles=legend_handles1, loc='upper right')

# Create a legend for marker sizes
legend2 = plt.legend(handles=legend_handles2, loc='lower left', title='Record length (years)', fontsize=10, title_fontsize=10, frameon=False)

# Add the first legend back to the axes
plt.gca().add_artist(legend1)

# Set the position of legend 2 relative to the axes
plt.gca().add_artist(legend2)

vmin=400 
vmax=1200 
scalar_mappable = plt.cm.ScalarMappable(cmap='summer') 
scalar_mappable.set_array([]) 
scalar_mappable.set_clim(vmin=vmin, vmax=vmax)
cbar = plt.colorbar(scalar_mappable, ax=ax, orientation='horizontal', label='Mean precipitation (mm/year)', pad=-0.22, alpha = 0.8,shrink=0.3,extend='both') 
cbar.ax.xaxis.set_label_position('top')  # Move label to the top
cbar.ax.tick_params(labelsize=10)  # Adjust tick label size
cbar.ax.xaxis.labelpad = 5

cbar.ax.set_position([cbar.ax.get_position().x0 - 0.09, cbar.ax.get_position().y0-0.1, 
                      cbar.ax.get_position().width, cbar.ax.get_position().height])

ax.text(0.49, 0.3, 'Nueces R.', transform=ax.transAxes, fontsize=8,rotation = -75, color='dodgerblue')
ax.text(0.61, 0.29, 'San Antonio R.', transform=ax.transAxes, fontsize=8,rotation = -33, color='dodgerblue')
ax.text(0.41, 0.58, 'Colorado R.', transform=ax.transAxes, fontsize=8,rotation = -40, color='dodgerblue')
ax.text(0.6, 0.53, 'Brazos R.', transform=ax.transAxes, fontsize=8,rotation = -58, color='dodgerblue')
ax.text(0.75, 0.45, 'Trinity R.', transform=ax.transAxes, fontsize=8,rotation = -33, color='dodgerblue')
ax.text(0.8, 0.505, 'Neches R.', transform=ax.transAxes, fontsize=8,rotation = -40, color='dodgerblue')
ax.text(0.75, 0.60, 'Sabine R.', transform=ax.transAxes, fontsize=8,rotation = -24, color='dodgerblue')

ax.tick_params(axis='both', which='both', length=0)
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.savefig(path + 'Fig_1.png',dpi=600,bbox_inches='tight')