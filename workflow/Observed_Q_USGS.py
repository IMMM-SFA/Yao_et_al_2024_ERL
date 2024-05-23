# This script is extract the observed Q from USGS

# __author__ = 'Lili Yao'
# __email__  = 'lili.yao@pnnl.gov'

import dataretrieval.nwis as nwis
site = '########' # The desired USGS gauge number
dftem1 = nwis.get_record(site=site,service = 'dv', start='1967-01-01', end='1998-12-31',parameterCd='00060',verify=False) # Customize the start and end date
dftem2 = dftem1.reset_index()
dftem2['date']=dftem2['datetime'].dt.date
df = dftem2[['date','site_no','00060_Mean','00060_Mean_cd']].copy()
df.rename(columns={'date':'date','site_no':'site_no','00060_Mean':'daily mean Q (cfs)','00060_Mean_cd':'code'},inplace=True)
df.to_csv('/path/to/save/folder/'+site+'.csv',index=False) 
