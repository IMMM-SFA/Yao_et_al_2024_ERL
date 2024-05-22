# This script is for calculating the SPI using the monthly precipitation data, and extract meteorological drought based on run theory. 

# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import pandas as pd
import numpy as np
import xarray 
import scipy.stats
from scipy.stats import rankdata
import os

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


################################################ SPI  ################################################

P_drought_threshold = -0.5
threshold2 = 0.5

River_list = ['Nueces','San_Antonio','Colorado','Brazos','Trinity','Neches','Sabine']

scenario = 'nat' # gaged, nat
for River in River_list:
    path= '/path/to/area/weighted/prec/folder/' + River + '_River/weighted_prec/'
    df_gage = pd.read_csv(path + 'gage_list.csv',header=None)
    gage_list = df_gage.iloc[:,0].tolist()
    path_timescale = '/path/to/response/time/folder/' + River + '_River/weighted_prec/pcc_SSI1_SPI-N/'
    df_timescale = pd.read_csv(path_timescale + 'max_pcc_with_SSI1-lognormal.csv', header = 0)
    timescale = df_timescale['max_timescale_' + scenario].values.tolist()
    path_SPI = '/path/to/SPI/foler/' + River + '_River/weighted_prec/SPI/'
    if not os.path.exists(path_SPI):
        os.makedirs(path_SPI)
        
    for i,gage_tem in enumerate(gage_list):
        gage = str(int(0)) + str(int(gage_tem))
        df = pd.read_csv(path + gage + '.csv',header=0)
        df['date'] = pd.to_datetime(df['date'])
        df['date'] = pd.to_datetime(df['date'])
        df['date'] = df['date'] + pd.offsets.MonthEnd(0)
        first_year = df['date'].dt.year.min()
        last_year = df['date'].dt.year.max()
        spi_value_gamma = my_spi(df['weighted_prec'].values,df['weighted_prec'].values,timescale[i],'gamma',3.09,-3.09)
        df['spi'] =  spi_value_gamma
        spi_value_gamma = np.nan_to_num(spi_value_gamma, nan=0)
        below_threshold = spi_value_gamma  < P_drought_threshold

        runs = np.split(df.index, np.where(np.diff(below_threshold.astype(int)))[0] + 1)
        # Calculate duration and severity of each drought event
        drought_events = []
        prev_drought_end = None  # Initialize variable to store the end date of the previous drought event
        for run in runs:
            if below_threshold[run[0]]:
                drought_start = df.loc[run[0], 'date']
                drought_end = df.loc[run[-1], 'date']
                # Calculate duration 
                duration = (drought_end.year - drought_start.year) * 12 + (drought_end.month - drought_start.month) + 1
                severity = df.loc[run, 'spi'].sum()  

                if prev_drought_end is not None:
                    interval_ssi = df.loc[(df['date'] > prev_drought_end) & (df['date'] < drought_start), 'spi']
                    mean_interval_ssi = interval_ssi.mean()
                    # If the intervalbetween the end and onset months of two consecutive drought events was less than 3 months 
                    # and the mean SPI value during this period was less than 0.5, they were merged into a single drought event.
                    if (drought_start.year - prev_drought_end.year) * 12 + (drought_start.month - prev_drought_end.month) <= 3 and mean_interval_ssi < threshold2:
                        drought_events[-1]['end_date'] = drought_end  
                        drought_events[-1]['duration'] += duration  
                        drought_events[-1]['severity'] += severity  
                    else:
                        drought_events.append({'start_date': drought_start, 'end_date': drought_end, 'duration': duration, 'severity': severity})
                else:
                    drought_events.append({'start_date': drought_start, 'end_date': drought_end, 'duration': duration, 'severity': severity})
                prev_drought_end = drought_end

        drought_df = pd.DataFrame(drought_events)
        drought_df['category'] = categorize_values(drought_df['severity'].values)
        drought_df.to_csv(path + 'SPI/' + gage +'_drought_event_SPI' + str(int(timescale[i]))+ '.csv',index= False)
        df.to_csv(path + 'SPI/' + gage +'_SPI' + str(int(timescale[i]))+ '.csv',index= False)