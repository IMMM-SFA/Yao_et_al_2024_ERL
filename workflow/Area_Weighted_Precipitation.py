# This script is for creating the area_weighted_precipitation at the monthly scale for each USGS streamflow gauge, 
# based on the drainage area coverage within each TX precipitation quadrangle. 

# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import pandas as pd
import numpy as np
from climate_indices import compute, indices
from climate_indices.indices import spi, Distribution
from climate_indices.compute import Periodicity


River_list = ['Nueces','San_Antonio','Colorado','Brazos','Trinity','Neches','Sabine']

for River in River_list:
    river_name = River + '_River'
    path = '/path/to/the/base/directory/'
    df_mapping = pd.read_csv(path + 'degtxt_quads_mapping.csv',header=0)
    df_prec = pd.read_csv(path + 'all_quads_precipitation_inch.csv',header=0)
    df_gage = pd.read_csv(path + river_name +'/gage_list.csv',header=None)
    for n in range(len(df_gage)):
        gage_tem = df_gage.iloc[n,0]
        gage = str(int(gage_tem))
        df = pd.read_csv(path + river_name +'/'+gage + '.csv',header=0)
        df['area_fraction'] = [a/np.sum(df['area2']) for a in df['area2']]
        merged_df = pd.merge(df, df_mapping, on="DEGTXT", how="left")
        merged_df.drop(columns=['AREA', 'PERIMETER', 'TX_1DEG_GR','DEGNUM','WEST_BND','EAST_BND','NORTH_BND','SOUTH_BND','TX_1DEG__1'], inplace=True)
        merged_df['quads'] = merged_df['quads'].astype(str)
        quads_gages = merged_df['quads'].astype(str)
        prec_columns =  ['date'] + list(quads_gages)
        prec_data = df_prec[prec_columns] 
        for quads_gage in quads_gages:
            # Multiply the precipitation column by the area_fraction
            prec_data[quads_gage] = prec_data[quads_gage] * merged_df.loc[merged_df['quads'] == quads_gage, 'area_fraction'].values[0]
        prec_sum = prec_data.drop(columns='date').sum(axis=1)
        prec_data['weighted_prec'] = prec_sum
        df_new = prec_data[['date','weighted_prec']].iloc[0:924, :] # Customize it based on the interested period record 
        df_new.to_csv(path + river_name +'/weighted_prec/0' + gage + '.csv', index=False)