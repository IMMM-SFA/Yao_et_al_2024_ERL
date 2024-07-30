# This script is to calculate the relative change in monthly cumulative drought months and severity between natural and managed conditions. 

# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import pandas as pd
import numpy as np 

River_list = ['Nueces','San_Antonio','Colorado','Brazos','Trinity','Neches','Sabine']

monthly_trend_counts = []


for month in range(1,13):
    dry_count_nat = 0     
    dry_count_gaged = 0   
     
    for River in River_list:
        path_nat = '/path/to/naturalized_Q/'+River+'_River_natQ/'
        path_gaged = '/path/to/gaged_Q/'+River+'_River_gagedQ/'
        df_gage = pd.read_csv(path_nat + 'gage_list.csv',header=None)

        for n in range(len(df_gage)):
            
            dry_count_nat = 0     
            dry_count_gaged = 0 
    
            gage_tem = df_gage.iloc[n,0]
            point_id = df_gage.iloc[n,1]
            gage = str(int(0)) + str(int(gage_tem))
            
            df_nat = pd.read_csv(path_nat+ gage + '_SSI-1_lognormal.csv')
            df_nat['date'] = pd.to_datetime(df_nat['date'])
            df_nat['month'] = df_nat['date'].dt.month
            
            df_gaged = pd.read_csv(path_gaged+ gage + '_SSI-1_lognormal.csv')
            df_gaged['date'] = pd.to_datetime(df_gaged['date'])
            df_gaged['month'] = df_gaged['date'].dt.month

            monthly_data_nat = df_nat[df_nat['month'] == month]['ssi-1'].values
            dry_count_nat += (monthly_data_nat < -0.5).sum()
            dry_sum_nat = np.abs(monthly_data_nat[monthly_data_nat < -0.5].sum())
            
            monthly_data_gaged = df_gaged[df_gaged['month'] == month]['ssi-1'].values
            dry_count_gaged += (monthly_data_gaged < -0.5).sum()
            dry_sum_gaged = np.abs(monthly_data_gaged[monthly_data_gaged < -0.5].sum())
            if dry_count_nat!=0:
                count_change = (dry_count_gaged-dry_count_nat)/dry_count_nat*100.0 
                severity_change = (dry_sum_gaged - dry_sum_nat)/dry_sum_nat*100.0 
            else: 
                count_change = np.nan
                severity_change = np.nan     
            print (month, gage, severity_change,count_change) 