# This script is for calculating the meteorological-hydrological drought propagation rate. 

# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import pandas as pd
import numpy as np

ssi_distribution = 'lognormal' 
threshold = -0.5
threshold2 = 0.5

River_list = ['Nueces','San_Antonio','Colorado','Brazos','Trinity','Neches','Sabine']
scenario = 'gaged' # gaged, nat

for River in River_list:
    path= '/path/to/area/weighted/precipitation/folder/' + River + '_River/weighted_prec/'
    df_gage = pd.read_csv(path + 'gage_list.csv',header=None)
    gage_list = df_gage.iloc[:,0].tolist()
    path_timescale = '/path/to/response/timescale/folder/' + River + '_River/weighted_prec/pcc_SSI1_SPI-N/'
    df_timescale = pd.read_csv(path_timescale + 'max_pcc_with_SSI1-lognormal.csv', header = 0)
    timescale = df_timescale['max_timescale_' + scenario].values.tolist()
    path_M_drought = '/path/to/SPI/folder' + River + '_River/weighted_prec/SPI/'
   
    path_Q = '/path/to/streamflow/folder/' + River +'_River_' + scenario + 'Q/'

    df_char = pd.DataFrame()
    for i,gage_tem in enumerate(gage_list):
        gage = str(int(0)) + str(int(gage_tem))
        df = pd.read_csv(path_Q + gage + '_SSI-1_'+ssi_distribution+'.csv')
        df['date'] = pd.to_datetime(df['date'])
        # Identify runs where SSI is below threshold
        below_threshold = df['ssi-1'] < threshold
        runs = np.split(df.index, np.where(np.diff(below_threshold.astype(int)))[0] + 1)
        drought_events = []
        prev_drought_end = None  # Initialize variable to store the end date of the previous drought event
        for run in runs:
            if below_threshold[run[0]]:
                drought_start = df.loc[run[0], 'date']
                drought_end = df.loc[run[-1], 'date']
                if prev_drought_end is not None:
                    interval_ssi = df.loc[(df['date'] > prev_drought_end) & (df['date'] < drought_start), 'ssi-1']
                    mean_interval_ssi = interval_ssi.mean()
                    # If the intervalbetween the end and onset months of two consecutive drought events was less than 3 months 
                    # and the meanSPI/SRI value during this period was less than 0.5, they were merged into a single drought event.
                    if (drought_start.year - prev_drought_end.year) * 12 + (drought_start.month - prev_drought_end.month) <= 3 and mean_interval_ssi < threshold2:
                        drought_events[-1]['end_date'] = drought_end  
  
                    else:
                        drought_events.append({'start_date': drought_start, 'end_date': drought_end})
                else:
                    drought_events.append({'start_date': drought_start, 'end_date': drought_end})
                prev_drought_end = drought_end
        
        df_H_drought = pd.DataFrame(drought_events)

        df_M_drought = pd.read_csv(path_M_drought + gage + '_drought_event_SPI' + str(int(timescale[i])) +'.csv',header=0)
        
        matched_droughts = []
        for index, meteo_drought_row in df_M_drought.iterrows():
            meteo_drought_start = meteo_drought_row['start_date']
            meteo_drought_end = meteo_drought_row['end_date']  
            # Check if there's a hydrological drought that overlaps with the meteorological drought
            overlap = ((df_H_drought['start_date'] <= meteo_drought_end) & (df_H_drought['end_date'] >= meteo_drought_start))    
            matched_hydro_droughts = df_H_drought[overlap]
            if not matched_hydro_droughts.empty:
                matched_droughts.append({'meteo_start_date': meteo_drought_start,
                                        'meteo_end_date': meteo_drought_end,
                                        'matched_hydro_droughts': matched_hydro_droughts})
        # Concatenate all matched hydrological droughts into one DataFrame
        if matched_droughts:
            matched_hydro_droughts_df = pd.concat([d['matched_hydro_droughts'] for d in matched_droughts])
        matched_drought_count = len(matched_droughts)
        meto_drought_count = len(df_M_drought)
        rate = matched_drought_count/meto_drought_count
        print (gage,scenario, rate)
