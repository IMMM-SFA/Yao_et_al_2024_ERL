[![DOI](https://zenodo.org/badge/265254045.svg)](https://zenodo.org/doi/10.5281/zenodo.10442485)

# Yao_et_al_2024_ERL
**Assessing the Complex Influences of Water Management on Hydrological Drought Characteristics in Texas**  
  
Lili Yao<sup>1*</sup>, Stephen B Ferencz<sup>1</sup>, Ning Sun<sup>1</sup>, Hongxiang Yan<sup>1</sup>  
  
<sup>1</sup> Pacific Northwest National Laboratory, Richland, WA., USA  
  
<sup>*</sup> corresponding author: lili.yao@pnnl.gov

## Abstract
The state of Texas in the United States is highly susceptible to drought. Its major rivers are subject to extensive water management (WM) activities in order to sustain multisectoral water demands, particularly during drought conditions. However, the impact of WM on the propagation dynamics and characteristics of hydrological drought (HD) in Texas remains unclear. To fill this gap, this study quantifies the influence of WM across 32 streamflow gauges along the mainstems of seven major rivers in Texas by comparing a variety of drought metrics under natural and managed conditions. Notably, we leveraged an extensive, naturalized streamflow dataset constructed by the Texas Commission on Environmental Quality (TCEQ), paired with gauge observations of managed conditions. Results indicate that at the multi-decadal scale, WM significantly reduced HD frequency across all seven rivers and at 81% of the gauges analyzed. Additionally, it increased the response timescale of HD across Texas’ major rivers by a median of 2.5 months. Conversely, the average-event duration and severity increased in most locations. Temporal analysis reveals that the WM impact on HD varied seasonally, with attenuation effects during mid-summer and early fall and intensification effects during late winter and spring. Additionally, WM was found to greatly increase the spatial variability of HD characteristics across the region. These findings emphasize the complexity of WM effects on HD and the necessity for nuanced strategies in managing HD under WM influences. 

## Journal reference
Yao, L., Ferencz, SB., Sun, N., Yan, H. (2024) Environmental Research Letters, October 2024, 19(11):114034, DOI:10.1088/1748-9326/ad7d23

## Data reference  
### Input data  
1. Precipitation data from Texas Water Development Board
   * Retrived from https://waterdatafortexas.org/lake-evaporation-rainfall

2. Observed streamflow data from USGS National Water Information System (NWIS)
   * Retrived using a python package, i.e., dataretrieval, https://github.com/DOI-USGS/dataretrieval-python?tab=readme-ov-file
    
3. Naturalized streamflow data from WRAP basin model
   * Retrived from https://www.tceq.texas.gov/permitting/water_rights/wr_technical-resources/wam.html for the FLO file.

4. River flowline data from National Hydrography Dataset Plus (NHDPlus) Data
   * Retrived from https://www.epa.gov/waterdata/nhdplus-texas-data-vector-processing-unit-12

6. Streamflow gauge drainage area boundary from Hydro Network-Linked Data Index (NLDI)
   * Retrieved from https://waterdata.usgs.gov/blog/nldi-intro/

8. Texas-Gulf basin (HUC2=12) boundary from the National Map developed by USGS
   * Retrived from https://waterdata.usgs.gov/blog/nldi-intro/
   
10. The location of the major reservoirs from Texas Water Development Board GIS dataset
    * Retrieved from https://www.twdb.texas.gov/mapping/gisdata/doc/Existing_Reservoirs.zip
      
11. The 1 degree by 1 degree state grids from Texas Water Development Board GIS dataset
    * Retrieved from https://www.twdb.texas.gov/mapping/gisdata/doc/state_grids.zip
         
12. The boundary of the Texas from Texas Department of Transportation
    * Retrived from https://gis-txdot.opendata.arcgis.com/datasets/TXDOT::texas-state-boundary/explore?location=30.834886%2C-100.077018%2C6.08

### Output data
Output data for each drought characteristics saved in the 'plot.csv' under the 'Plot.zip'

## Reproduce my experiment
1. Download 'Observed_Q.zip', 'Naturalized_Q.zip', and 'Precipitation.zip' folders for the input data, and download the 'Plot.zip' for the output data which including the final results supporting the analysis in this study.
2. The 'Observed_Q', 'Naturalized_Q', and 'Precipitation' folders were used for saving and processing the observed streamflow, naturalized flow, and precipitation data, respectively. To facilitate data processing, the data for each gauge in the same river basin were saved in folders named after the river within each of the 'Observed_Q', 'Naturalized_Q', and 'Precipitation' folders. The gauge name list for each river can be found in these river folders. The streamflow gauges in the WRAP FLO file do not appear as USGS gauge numbers; instead, they have ID numbers in the WRAP model. The mapping between the WRAP gauge IDs and the USGS gauge numbers was saved in the gauge name list file.
3. Run 'Observed_Q_USGS.py' to extract observed flow from USGS. 
5. The raw FLO file from WRAP model was saved in 'FLO' folder under the 'Naturalized_Q'. Run 'Natural_Q_WRAP.py' to extract the naturalized flow from FLO file and save in csv format. To facilit data processing, the naturalized Q for each gauge was then saved in separate csv file in the river folder under 'Naturalized_Q'.
6. The raw monthly precipitation data from TWDB was saved in 'all_quads_precipitation_inch.csv' in the 'Precipitation' folder. The 'DrainageArea' folder contains the drainage area boundary shp file for each gauge. The state 1-degree grids shp file was saved in 'DrainageArea_in_TX_1degree' folder under 'Precipitation'. The GIS clip function was used to extract state 1-degree grid features overlaying the gauge drainage area which was saved in 'DrainageArea_in_TX_1degree'. The drainage area coverage for each gauge within each quadrangle was exported from the attribute table and saved as a csv file named after the gauge number in each river folder in 'Precipitation'. The state 1-degree grid numbers differ from those shown on the TWDB quadrangles precipitation data webpage. The mapping between them was saved in 'degtxt_quads_mapping.csv' in 'Precipitation'.
7. Run 'Area_Weighted_Precipitation.py' to get the area weighted monthly precipitation for each gauge.
8. Run 'Standardized_Streamflow_Index.py' to calculate the 1-month standardized streamflow index for regualted flow and natual flow at the monthly scale.
10. Run 'M-H_Response_Time.py' to calcualte the meteorological-hydrological drought response time.
11. Run 'M-H_Propagation_Rate.py' to calculate the meteorological-hydrological drought propagation rate.
12. Run 'Meteorological_Drought.py' to identify meteorological drought events.
13. Run 'Hydrological_Drought.py' to identify hydrological drought events, and extract the drought characteristics.
15. Merge all the outputs into one csv file ('plot.csv') and save in the 'Plot' folder
16. Run 'Relative_change_monthly_occurrence_severity.py' to calculate the relative change in monthly cumulative drought months and severity between natural and managed conditions. Save the results in 'Monthly_analysis' folder under 'Plot' folder.
17. The shp file for Texas state boundary, Texas-Gulf basin boundary, river mainstems, reservoirs, and gauge stations were saved in the 'Plot' folder.
18. Use the plotting scripts to plot outputs.

## Reproduce my figures 
Use Fig_#.py from the 'workflow' folder to generate Fig. 1 to Fig. 8.


