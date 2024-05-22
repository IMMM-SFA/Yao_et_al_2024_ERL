# This script is for calculating the response time of hydrological drought to meteorological drought based on correlation analysis.

# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import os 



ssi_distribution = 'lognormal'
River_list = ['Nueces','San_Antonio','Colorado','Brazos','Trinity','Neches','Sabine']

for River in River_list:
    print (River)
    path= '/path/to/area_weighted_prec/' + River + '_River/weighted_prec/'
    path_gagedssi = '/path/to/SSI_observedQ/' + River + '_River_observedQ/'
    path_natssi = '/path/to/SSI_naturalizedQ/' + River + '_River_natQ/'
    df_gage = pd.read_csv(path + 'gage_list.csv',header=None)
    path2 = path + 'pcc_SSI1_SPI-N/'
    if not os.path.exists(path2):
        os.makedirs(path2)
    
    gage_list, point_id_list, max_timescale_gaged_list, max_timescale_nat_list, max_pcc_gaged_list, max_pcc_nat_list = [], [], [], [], [], []
    for n in range(len(df_gage)):
        gage_tem = df_gage.iloc[n,0]
        gage = str(int(0)) + str(int(gage_tem))
        gage_list.append(gage)
        point_id_list.append(df_gage.iloc[n,1])
        df_gagedssi = pd.read_csv(path_gagedssi + gage + '_SSI-1_' + ssi_distribution + '.csv',header=0) 
        df_natssi = pd.read_csv(path_natssi + gage + '_SSI-1_'+ ssi_distribution +'.csv',header=0) 
        df = pd.read_csv(path + gage + '.csv',header=0)
        df['date'] = pd.to_datetime(df['date'])
        first_year = df['date'].dt.year.min()
        last_year = df['date'].dt.year.max()
        df.set_index('date', inplace=True)
        pcc_list_gaged = []
        p_value_list_gaged = []
        pcc_list_nat = []
        p_value_list_nat= [] 
        time_scale_list = []
        df_pcc = pd.DataFrame()
        df_pcc_max = pd.DataFrame()
        max_pcc_gaged = -np.inf
        max_pcc_nat = -np.inf
        max_timescale_gaged = None
        max_timescale_nat = None

        for m in range(1,37):
            time_scale_list.append(m)
            gaged_ssi = df_gagedssi['ssi-1'].values
            nat_ssi = df_natssi['ssi-1'].values
            spi_value_gamma = my_spi(df['weighted_prec'].values,df['weighted_prec'].values,m,'gamma',3.09,-3.09)
            valid_indices_gaged = ~np.isnan(gaged_ssi) & ~np.isnan(spi_value_gamma)
            valid_indices_nat = ~np.isnan(nat_ssi) & ~np.isnan(spi_value_gamma)
            gaged_ssi = gaged_ssi[valid_indices_gaged]
            nat_ssi = nat_ssi[valid_indices_nat]
            spi_value_gamma_for_gaged = spi_value_gamma[valid_indices_gaged]
            spi_value_gamma_for_nat = spi_value_gamma[valid_indices_nat]
            corr_coefficient_gaged, p_value_gaged = pearsonr(gaged_ssi , spi_value_gamma_for_gaged)
            corr_coefficient_nat, p_value_nat = pearsonr(nat_ssi , spi_value_gamma_for_nat)
            pcc_list_gaged.append(corr_coefficient_gaged)
            p_value_list_gaged.append(p_value_gaged)   
            pcc_list_nat.append(corr_coefficient_nat)
            p_value_list_nat.append(p_value_nat)         

            if corr_coefficient_gaged > max_pcc_gaged:
                max_pcc_gaged = corr_coefficient_gaged
                max_timescale_gaged = m

            if corr_coefficient_nat > max_pcc_nat:
                max_pcc_nat = corr_coefficient_nat
                max_timescale_nat = m

        df_pcc['time_scale'] = time_scale_list
        df_pcc['pcc_gaged'] = pcc_list_gaged
        df_pcc['pcc_nat'] = pcc_list_nat
        df_pcc['pvalue_gaged'] = p_value_list_gaged
        df_pcc['pvalue_nat'] = p_value_list_nat 
        
        max_timescale_gaged_list.append(max_timescale_gaged)
        max_timescale_nat_list.append(max_timescale_nat)
        max_pcc_gaged_list.append(round(max_pcc_gaged, 3))
        max_pcc_nat_list.append(round(max_pcc_nat, 3))
        print(gage, max_timescale_gaged,max_timescale_nat,round(max_pcc_gaged,3),round(max_pcc_nat,3),)
        df_pcc_max['PCP_id'] = point_id_list
        df_pcc_max['gage'] = gage_list
        df_pcc_max['max_timescale_gaged'] = max_timescale_gaged_list
        df_pcc_max['max_timescale_nat'] = max_timescale_nat_list
        df_pcc_max['max_pcc_gaged'] = max_pcc_gaged_list
        df_pcc_max['max_pcc_nat'] = max_pcc_nat_list
        df_pcc.to_csv(path + 'pcc_SSI1_SPI-N/' + gage + '_pcc_with_SSI1-'+ssi_distribution+'.csv',index = False)
    df_pcc_max.to_csv(path + 'pcc_SSI1_SPI-N/' + 'max_pcc_with_SSI1-'+ssi_distribution + '.csv',index = False)        
