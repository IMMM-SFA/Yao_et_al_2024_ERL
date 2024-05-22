# This script is for calculating the SSI using the observed Q or the naturalized Q. 

# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'


import xarray 
import numpy as np
import scipy.stats
import pandas as pd
from scipy.stats import rankdata

################################################ Define the function to calculate the standardied index  ################################################

def mean_calculation(data, temporal_scale):  
    # Calculate the mean of n months (temporal_scale) data
    data_mean = np.convolve(data, np.ones(temporal_scale)/temporal_scale, 'valid')
    data_mean = np.concatenate([[np.nan]*(temporal_scale-1), data_mean])
    n_year_incomplete = len(data_mean)/12 - int(len(data_mean)/12)
    n_month_incomplete = int(n_year_incomplete * 12)
    data_mean = np.concatenate([data_mean, [np.nan]*(n_month_incomplete)])
    data_mean_reshape = data_mean.reshape(int(len(data_mean)/12), 12)
    df = pd.DataFrame(data_mean_reshape)
    return data_mean_reshape

def lognormal_transformation(calibration, calculation, temporal_scale):
    
    zeros = (calibration == 0).sum(axis=0)
    p_zero = zeros / calibration.shape[0]
    
    calibration[calibration == 0] = np.NaN
    calibration_no_nan=calibration[~np.isnan(calibration)]
    
    log_calibration_no_nan = np.log(calibration_no_nan)
    mu = np.nanmean(log_calibration_no_nan, axis=0)
    sigma = np.nanstd(log_calibration_no_nan, axis=0)
    scale = np.exp(mu)
    
    zero_indices_calculation = np.where(calculation == 0)
    calculation[calculation == 0] = np.NaN
    p_lognormal_non_zero =  scipy.stats.lognorm.cdf(calculation, s=sigma, scale=scale)
    p_lognormal = p_zero + (1 - p_zero) * p_lognormal_non_zero
    for row_index, col_index in zip(*zero_indices_calculation):
        p_lognormal[row_index, col_index] = p_zero[col_index]
    calculation_transformed = scipy.stats.norm.ppf(p_lognormal)
    calculation_transformed = calculation_transformed.flatten()
    return calculation_transformed


def my_spi(precipitation_calibration:np.ndarray,precipitation_calculation:np.ndarray,temporal_scale:int,distribution = 'gamma',upper_limit = 3.09,lower_limit = -3.09):

    # upper_limit, lower_limit: The maximum and minimum SPI values, according to https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1752-1688.1999.tb03592.x , the default values are 3.09 and -3.09.
    # Theoretically, the SPI is unbounded. Practically,however, the number of observations of the precipitation data, which is generally less than 100 for a givenmonth, season or other time period, for locations inthe United States, suggests bounds of ± 3.09. Thesebounds correspond to probabilities of .999 and .001and return periods of one in 1,000. Estimation of more extreme probabilities, based on sample sizes of only100, is likely to be inaccurate. 
    
    #The precipitation values should be non-negative.
    if precipitation_calibration[~np.isnan(precipitation_calibration)].min()<0:
        print("All negative values will be assign to be 0")
        precipitation_calibration.clip(min=0)
    if precipitation_calculation[~np.isnan(precipitation_calculation)].min()<0:
        print("All negative values will be assign to be 0")
        precipitation_calculation.clip(min=0)
        
    length_input = len(precipitation_calibration)
    #calculate the monthly mean precipitation of calibration and calculation data, then reshape them to 2-d array.
    precipitation_calibration_mean = mean_calculation(precipitation_calibration,temporal_scale)
    precipitation_calculation_mean = mean_calculation(precipitation_calculation,temporal_scale)
    # print ('precipitation_calibration_mean',precipitation_calibration_mean)
    # apply the gamma transformation to monthly mean data
    if distribution == 'gamma':
        spi_n = gamma_transformation(precipitation_calibration_mean,
                                    precipitation_calculation_mean,
                                    temporal_scale)
        
    elif distribution == 'lognormal':
        spi_n = lognormal_transformation(precipitation_calibration_mean,
                                    precipitation_calculation_mean,
                                    temporal_scale)
    # clip the spi values 
    spi_n = np.clip(spi_n,a_min=lower_limit , a_max=upper_limit)
    #change spi_n to its original length 
    spi_n =  spi_n[0:length_input]
    return spi_n


################################################ SSI of observed Q  ################################################

River_list = ['Nueces','San_Antonio','Colorado','Brazos','Trinity','Neches','Sabine']
for River in River_list:
    print (River)
    path = '/path/to/observed_Q/'+River+'_River_observedQ/'
    path_natQ = '/path/to/naturalized_Q/'+River+'_River_natQ/'

    df_gage = pd.read_csv(path + 'gage_list.csv',header=None)
    temporal_scale = 1 # unit:month
    for n in range(len(df_gage)):
        gage_tem = df_gage.iloc[n,0]
        gage = str(int(0)) + str(int(gage_tem))
        df_D = pd.read_csv(path + 'cfs/'+ gage + '.csv',header=0)
        df_D['date'] = pd.to_datetime(df_D['date'])
        first_year = df_D['date'].dt.year.min()
        last_year = df_D['date'].dt.year.max()
        df_D.set_index('date', inplace=True)
        df_D['daily_mean_Q_cfd'] = df_D.iloc[:,1].values * 24 * 3600 # convert the unit from "cubic feet per second" to "cubic feet per day"
        df_M_tem = df_D.resample('M').sum()
        df_M_tem['monthly_Q_afm'] = df_M_tem['daily_mean_Q_cfd']*2.29569e-5 # convert the unit from "cubic feet per month" to "acre feet per month"
        df_M = df_M_tem[['monthly_Q_afm']].copy()
        df_M.to_csv(path  + gage + '_monthly_Q.csv', index = True)
        Q_M = df_M['monthly_Q_afm'].values
        df_M_natQ = pd.read_csv(path_natQ +gage + '.csv',header=0)
        Q_M_natQ = df_M_natQ[str(int(gage_tem))].values
        Q_M = Q_M.astype(float)
        Q_M_natQ = Q_M_natQ.astype(float)
        ssi_value = my_spi(Q_M_natQ,Q_M,temporal_scale,'lognormal',3.09,-3.09) 
        col_name = 'ssi-' + str(int(temporal_scale))
        df_M[col_name] = ssi_value
        df_M.to_csv(path  +gage + '_SSI-' + str(int(temporal_scale)) + '_lognormal.csv', index = True)

################################################ SSI of naturalized Q  ################################################
River_list = ['Nueces','San_Antonio','Colorado','Brazos','Trinity','Neches','Sabine']

for River in River_list:
    print (River)
    path = '/path/to/naturalized_Q/'+River+'_River_natQ/'
    df_gage = pd.read_csv(path + 'gage_list.csv',header=None)
    temporal_scale = 1 # unit:month
    for n in range(len(df_gage)):
        gage_tem = df_gage.iloc[n,0]
        gage = str(int(0)) + str(int(gage_tem))
        df_M = pd.read_csv(path +gage + '.csv',header=0)
        df_M['date'] = pd.to_datetime(df_M['date'])
        first_year = df_M['date'].dt.year.min()
        last_year = df_M['date'].dt.year.max()
        df_M.set_index('date', inplace=True)
        Q_M = df_M[str(int(gage_tem))].values
        Q_M = Q_M.astype(float)
        ssi_value = my_spi(Q_M,Q_M,temporal_scale,'lognormal',3.09,-3.09) 
        col_name = 'ssi-' + str(int(temporal_scale))
        df_M[col_name] = ssi_value
        df_M.to_csv(path +gage + '_SSI-' + str(int(temporal_scale)) + '_lognormal.csv', index = True)