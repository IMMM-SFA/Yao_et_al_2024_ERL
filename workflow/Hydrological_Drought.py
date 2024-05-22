# This script is to identify hydrological drought events, and extract the drought characteristics 

# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import pandas as pd
import numpy as np

threshold = -0.5
threshold2 = 0.5

River_list = ['Nueces','San_Antonio','Colorado','Brazos','Trinity','Neches','Sabine']
scenario = 'nat' # gaged, nat

for River in River_list:
    path = '/path/to/streamflow/folder/' + River + '_River_' + scenario + 'Q/'
    df_gage = pd.read_csv(path + 'gage_list.csv',header=None)
    gage_list = []
    frequency_list = []
    duration_list = []
    severity_list = []
    total_duration_list = []
    total_severity_list = []
    df_char = pd.DataFrame()
    path_timescale = '/path/to/response/timescale/folder/' + River + '_River/weighted_prec/pcc_SSI1_SPI-N/'
    df_timescale = pd.read_csv(path_timescale + 'max_pcc_with_SSI1-lognormal.csv', header = 0)
    timescale_list = df_timescale['max_timescale_' + scenario].values.tolist()
    for n in range(len(df_gage)):
        gage_tem = df_gage.iloc[n,0]
        timescale = timescale_list[n]
        df_M_drought = pd.read_csv('/path/to/meteo/drought/event/folder/' + River + '_River/weighted_prec/SPI/' + '0'+str(gage_tem) +'_drought_event_SPI' + str(timescale) +'.csv',header=0)
        df_M_drought['start_date'] = pd.to_datetime(df_M_drought['start_date'])
        df_M_drought['end_date'] = pd.to_datetime(df_M_drought['end_date'])
        gage = str(int(0)) + str(int(gage_tem))
        gage_list.append(gage)
        df = pd.read_csv(path + gage + '_SSI-1_lognormal.csv')
        df['date'] = pd.to_datetime(df['date'])
        below_threshold = df['ssi-1'] < threshold
        runs = np.split(df.index, np.where(np.diff(below_threshold.astype(int)))[0] + 1)
        drought_events = []
        prev_drought_end = None 
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
        # match the hydrological drought to the meteorological drought
        drought_events_new = []
        for drought_event in drought_events:
            drought_start = drought_event['start_date']
            drought_end = drought_event['end_date']
            overlap = ((df_M_drought['start_date'] <= drought_end) & (df_M_drought['end_date'] >= drought_start)).any()
            if overlap==True:
                first_overlap_index = ((df_M_drought['start_date'] <= drought_end) & (df_M_drought['end_date'] >= drought_start)).idxmax()
                first_overlap_start_date = df_M_drought.loc[first_overlap_index, 'start_date']
                if drought_start < first_overlap_start_date:
                    drought_event['start_date'] = first_overlap_start_date
                    while df.loc[df['date'] == first_overlap_start_date, 'ssi-1'].iloc[0] > threshold:
                        first_overlap_start_date += pd.DateOffset(months=1)
                        first_overlap_start_date = first_overlap_start_date + pd.offsets.MonthEnd(0)
                    drought_event['start_date'] = first_overlap_start_date
                    drought_events_new.append(drought_event)
                else:
                    drought_events_new.append(drought_event)
            elif overlap==False:
                pass

        # calculate the duration and severity for each hydrological drought 
        for drought_event in drought_events_new:
            drought_start = drought_event['start_date']
            drought_end = drought_event['end_date']
            # Select SSI values between adjusted start date and end date
            ssi_values = df.loc[(df['date'] >= drought_start) & (df['date'] <= drought_end), 'ssi-1']
            # Calculate duration (number of months below threshold)
            duration = (ssi_values < threshold).sum()
            # Calculate severity (sum of SSI values below threshold)
            severity = ssi_values[ssi_values < threshold].sum()
            # Update duration and severity in the drought event dictionary
            drought_event['duration'] = duration
            drought_event['severity'] = severity     

        # Convert drought events to DataFrame
        drought_df = pd.DataFrame(drought_events_new)
        drought_df.to_csv(path + 'Drought_extraction/' + gage +'_drought_event_SSI1.csv',index= False)
        # Calculate average duration and severity
        avg_duration = round(drought_df['duration'].mean(), 2)
        avg_severity = abs(round(drought_df['severity'].mean(), 2))
        frequency_list.append(len(drought_df))
        duration_list.append(avg_duration)
        severity_list.append(avg_severity)
        total_duration_list.append(drought_df['duration'].sum())
        total_severity_list.append(abs(drought_df['severity'].sum()))
    df_char['gage'] =  gage_list
    df_char['frequency'] =  frequency_list
    df_char['ave_duration'] =  duration_list
    df_char['ave_severity'] =  severity_list
    df_char['total_duration'] =  total_duration_list
    df_char['total_severity'] =  total_severity_list
    df_char.to_csv(path+ 'Drought_extraction/' + 'Drought_average_SSI1.csv',index= False)