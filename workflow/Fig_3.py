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

########################################################## 08124000 nat ####################################################################################
data = pd.read_csv('/path/to/plotting/folder/propagation_analysis/08124000_nat.csv')
events_HD= pd.read_csv('/path/to/plotting/folder/propagation_analysis/08124000_drought_event_SSI1_nat.csv')
events_MD = pd.read_csv('/path/to/plotting/folder/propagation_analysis/08124000_drought_event_SPI1.csv')

events_HD['start_date'] = pd.to_datetime(events_HD['start_date']).apply(lambda x: x.replace(day=1))
events_HD['end_date'] = pd.to_datetime(events_HD['end_date']).apply(lambda x: x.replace(day=1))
events_MD['start_date'] = pd.to_datetime(events_MD['start_date']).apply(lambda x: x.replace(day=1))
events_MD['end_date'] = pd.to_datetime(events_MD['end_date']).apply(lambda x: x.replace(day=1))
data['date'] = pd.to_datetime(data['date']).apply(lambda x: x.replace(day=1))

fig, ax = plt.subplots(figsize=(9,3))

data['month_days'] = data['date'].dt.days_in_month

ax.bar(data['date'], data['ssi'], width=data['month_days'], align='edge', color='red', label='H drought', alpha=0.5)
ax.bar(data['date'], data['spi'], width=data['month_days'], align='edge', color='grey', label='M drought', alpha=0.6)

for _, row in events_HD.iterrows():
    start, end = row['start_date'], row['end_date']
    while start <= end:
        ax.fill_between([start, start + pd.offsets.MonthEnd(0)], [-3, -3], [-2.90, -2.90], color='black', alpha=0.5)
        start += pd.offsets.MonthBegin(1)

for _, row in events_MD.iterrows():
    start, end = row['start_date'], row['end_date']
    while start <= end:
        ax.fill_between([start, start + pd.offsets.MonthEnd(0)], [-0.6, -0.6], [-0.4, -0.4], color='black', alpha=0.5)
        start += pd.offsets.MonthBegin(1)

ax.set_ylim(-3, -0.5)
ax.set_xlim(data['date'].min(), data['date'].max())
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=0, fontsize=17)
plt.yticks(np.arange(-0.5, -3.5, -0.5),fontsize=17)
plt.ylabel('SPI-1 or SSI-1', fontsize=15)
plt.title('08124000, Natural condition', fontsize=18, pad=8)
plt.savefig('08124000_nat_event.png',dpi=600,bbox_inches='tight')
plt.show()

########################################################## 08124000 gauge ####################################################################################

data = pd.read_csv('/path/to/plotting/folder/propagation_analysis/08124000_gauge.csv')
events_HD= pd.read_csv('/path/to/plotting/folder/propagation_analysis/08124000_drought_event_SSI1_gauge.csv')
events_MD = pd.read_csv('/path/to/plotting/folder/propagation_analysis/08124000_drought_event_SPI1.csv')
events_HD['start_date'] = pd.to_datetime(events_HD['start_date']).apply(lambda x: x.replace(day=1))
events_HD['end_date'] = pd.to_datetime(events_HD['end_date']).apply(lambda x: x.replace(day=1))
events_MD['start_date'] = pd.to_datetime(events_MD['start_date']).apply(lambda x: x.replace(day=1))
events_MD['end_date'] = pd.to_datetime(events_MD['end_date']).apply(lambda x: x.replace(day=1))
data['date'] = pd.to_datetime(data['date']).apply(lambda x: x.replace(day=1))
fig, ax = plt.subplots(figsize=(9,3))

data['month_days'] = data['date'].dt.days_in_month

ax.bar(data['date'], data['ssi'], width=data['month_days'], align='edge', color='red', label='H drought', alpha=0.5)
ax.bar(data['date'], data['spi'], width=data['month_days'], align='edge', color='grey', label='M drought', alpha=0.6)

for _, row in events_HD.iterrows():
    start, end = row['start_date'], row['end_date']
    while start <= end:
        ax.fill_between([start, start + pd.offsets.MonthEnd(0)], [-3, -3], [-2.90, -2.90], color='black', alpha=0.5)
        start += pd.offsets.MonthBegin(1)

for _, row in events_MD.iterrows():
    start, end = row['start_date'], row['end_date']
    while start <= end:
        ax.fill_between([start, start + pd.offsets.MonthEnd(0)], [-0.6, -0.6], [-0.4, -0.4], color='black', alpha=0.5)
        start += pd.offsets.MonthBegin(1)

ax.set_ylim(-3, -0.5)

ax.set_xlim(data['date'].min(), data['date'].max())
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=0, fontsize=17)
plt.yticks(np.arange(-0.5, -3.5, -0.5),fontsize=15)
plt.ylabel('SPI-1 or SSI-1', fontsize=17)
plt.title('08124000, Managed condition', fontsize=18, pad=8)
plt.savefig('08124000_gauge_event.png',dpi=600,bbox_inches='tight')
plt.show()

########################################################## 08211000 nat ####################################################################################
data = pd.read_csv('/path/to/plotting/folder/propagation_analysis/08211000_nat.csv')
events_HD= pd.read_csv('/path/to/plotting/folder/propagation_analysis/08211000_drought_event_SSI1_nat.csv')
events_MD = pd.read_csv('/path/to/plotting/folder/propagation_analysis/08211000_drought_event_SPI2.csv')

events_HD['start_date'] = pd.to_datetime(events_HD['start_date']).apply(lambda x: x.replace(day=1))
events_HD['end_date'] = pd.to_datetime(events_HD['end_date']).apply(lambda x: x.replace(day=1))
events_MD['start_date'] = pd.to_datetime(events_MD['start_date']).apply(lambda x: x.replace(day=1))
events_MD['end_date'] = pd.to_datetime(events_MD['end_date']).apply(lambda x: x.replace(day=1))
data['date'] = pd.to_datetime(data['date']).apply(lambda x: x.replace(day=1))

fig, ax = plt.subplots(figsize=(9,3))

data['month_days'] = data['date'].dt.days_in_month

ax.bar(data['date'], data['ssi'], width=data['month_days'], align='edge', color='red', label='H drought', alpha=0.5)
ax.bar(data['date'], data['spi'], width=data['month_days'], align='edge', color='grey', label='M drought', alpha=0.6)

for _, row in events_HD.iterrows():
    start, end = row['start_date'], row['end_date']
    while start <= end:
        ax.fill_between([start, start + pd.offsets.MonthEnd(0)], [-3, -3], [-2.90, -2.90], color='black', alpha=0.5)
        start += pd.offsets.MonthBegin(1)

for _, row in events_MD.iterrows():
    start, end = row['start_date'], row['end_date']
    while start <= end:
        ax.fill_between([start, start + pd.offsets.MonthEnd(0)], [-0.6, -0.6], [-0.4, -0.4], color='black', alpha=0.5)
        start += pd.offsets.MonthBegin(1)

ax.set_ylim(-3, -0.5)
ax.set_xlim(data['date'].min(), data['date'].max())
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=0, fontsize=17)
plt.yticks(np.arange(-0.5, -3.5, -0.5),fontsize=17)
plt.ylabel('SPI-1 or SSI-1', fontsize=15)
plt.title('08211000, Natural condition', fontsize=18, pad=8)
plt.savefig('08211000_nat_event.png',dpi=600,bbox_inches='tight')
plt.show()

########################################################## 08211000 gauge ####################################################################################

data = pd.read_csv('/path/to/plotting/folder/propagation_analysis/08211000_gauge.csv')
events_HD= pd.read_csv('/path/to/plotting/folder/propagation_analysis/08211000_drought_event_SSI1_gauge.csv')
events_MD = pd.read_csv('/path/to/plotting/folder/propagation_analysis/08211000_drought_event_SPI6.csv')
events_HD['start_date'] = pd.to_datetime(events_HD['start_date']).apply(lambda x: x.replace(day=1))
events_HD['end_date'] = pd.to_datetime(events_HD['end_date']).apply(lambda x: x.replace(day=1))
events_MD['start_date'] = pd.to_datetime(events_MD['start_date']).apply(lambda x: x.replace(day=1))
events_MD['end_date'] = pd.to_datetime(events_MD['end_date']).apply(lambda x: x.replace(day=1))
data['date'] = pd.to_datetime(data['date']).apply(lambda x: x.replace(day=1))
fig, ax = plt.subplots(figsize=(9,3))

data['month_days'] = data['date'].dt.days_in_month

ax.bar(data['date'], data['ssi'], width=data['month_days'], align='edge', color='red', label='H drought', alpha=0.5)
ax.bar(data['date'], data['spi'], width=data['month_days'], align='edge', color='grey', label='M drought', alpha=0.6)

for _, row in events_HD.iterrows():
    start, end = row['start_date'], row['end_date']
    while start <= end:
        ax.fill_between([start, start + pd.offsets.MonthEnd(0)], [-3, -3], [-2.90, -2.90], color='black', alpha=0.5)
        start += pd.offsets.MonthBegin(1)

for _, row in events_MD.iterrows():
    start, end = row['start_date'], row['end_date']
    while start <= end:
        ax.fill_between([start, start + pd.offsets.MonthEnd(0)], [-0.6, -0.6], [-0.4, -0.4], color='black', alpha=0.5)
        start += pd.offsets.MonthBegin(1)

ax.set_ylim(-3, -0.5)

ax.set_xlim(data['date'].min(), data['date'].max())
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=0, fontsize=17)
plt.yticks(np.arange(-0.5, -3.5, -0.5),fontsize=15)
plt.ylabel('SPI-1 or SSI-1', fontsize=17)
plt.title('08211000, Managed condition', fontsize=18, pad=8)
plt.savefig('08211000_gauge_event.png',dpi=600,bbox_inches='tight')
plt.show()
