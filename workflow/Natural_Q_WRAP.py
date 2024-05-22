# This script is to identify hydrological drought events, and extract the drought characteristics 

# __author__ = 'Stephen B, Ferencz'
# __email__  = 'stephen.ferencz@pnnl.gov'

import pandas as pd
import numpy as np
import os 

# Set directory path to where CSVs of WRAP .FLO data are stored 
os.chdir("C:/Users/XXXXXX/OneDrive - PNNL/Documents/ERCOT/WRAP/WRAP_naturalized_flow_data")


flo_files = ['Brazos.csv', 'Colorado.csv',  'Guadalupe_San_Antonio.csv',
             'Neches.csv', 'Nueces.csv', 'Sabine.csv','Trinity.csv']

# Construct database array, row (year, month), and column labels 
master_flo_data = np.zeros((91*12, 453))
master_column_names = ['Year','Month'] # will be appended by control point IDs
master_column_basin_names = ['Year','Month'] # will be appended by basin IDs
master_flo_years  = np.linspace(1930,  2020, 91) # column of year labels 
master_flo_years = np.repeat(master_flo_years, 12) # column of month labels 
master_flo_months = np.tile([1, 2, 3, 4, 5, 6 , 7,
                               8, 9, 10, 11, 12],91)

master_flo_data[:,0] = master_flo_years
master_flo_data[:,1] = master_flo_months

total_ids = 2 # tracks column index to use for adding basin data to master database array 

for i in range(len(flo_files)):

    # Load basin data 
    flo = pd.read_csv(flo_files[i], header = None, names = ['ID','Year','Jan',
            'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    
    # get control point IDs
    ids = flo.ID.unique().tolist() # unique ids become columns
    basin_ids = np.repeat(flo_files[i][:-4], len(ids)).tolist() # repeated basin ID for each column
    
    # get start and end years for data 
    first_year = min(flo.Year) # used to find start row index 
    last_year =  max(flo.Year) # used to find end row index 
    total_years = last_year - first_year + 1 # number of years
    
    # create empty array to populate with basin flo data 
    formatted_flo_data = np.zeros((12*total_years, len(ids))) 
        
    # loop to format flo data into rows time and columns control points 
    for n in range(len(ids)): # for each ID
        subset = flo.where(flo.ID == ids[n])
        subset = subset.dropna()
        for t in range(total_years): # for each year 
            formatted_flo_data[t*12:(t+1)*12,n] = subset.iloc[t,2:]
            
    # append IDs to master_column_names 
    master_column_names = master_column_names + ids

    # append basin ID to master_column_basin_names
    master_column_basin_names = master_column_basin_names + basin_ids

    # copy data from formatted_flo_data into master_flo_data
    row_first_year = (first_year - 1930) * 12  
    row_last_year = (last_year - 1930 + 1) * 12 
    master_flo_data[row_first_year:row_last_year, total_ids:total_ids + len(ids)] = formatted_flo_data[:][:]
    total_ids += len(ids)          
    
# Convert numpy array to DataFrame
master_flo_df = pd.DataFrame(data = master_flo_data)
# Add Control Point IDs and Basin IDs as columns indices 
master_flo_df.columns = [master_column_names, master_column_basin_names]
# Export dataframe as CSV
master_flo_df.to_csv('Monthly_natural_flows_WRAP_basins.csv')

# Visualize streamflow data as a heatmap
import seaborn as sns 
import matplotlib.pyplot as plt
plt.figure(figsize = (30,10))
sns.heatmap(master_flo_df.iloc[:,2:], vmin = 0, vmax = 10000)