[![DOI](https://zenodo.org/badge/265254045.svg)](https://zenodo.org/doi/10.5281/zenodo.10442485)

# Yao_et_al_2024_ERL
**Assessing the Complex Influences of Water Management on Hydrological Drought Characteristics in Texas**  
  
Lili Yao<sup>1*</sup>, Stephen B Ferencz<sup>1</sup>, Ning Sun<sup>1</sup>, Hongxiang Yan<sup>1</sup>  
  
<sup>1</sup> Pacific Northwest National Laboratory, Richland, WA., USA  
  
<sup>*</sup> corresponding author: lili.yao@pnnl.gov

## Abstract
The state of Texas in the United States is highly susceptible to drought, and its major rivers are subject to extensive water management activities. Water management alters streamflow regimes, thereby influencing the propagation processes of drought from meteorological to hydrological types and changing the characteristics of hydrological drought. Nevertheless, the impact of water management on drought properties in Texas is not yet fully studied. This study aims to fill this gap by leveraging an extensive observation-based naturalized streamflow dataset constructed by the Texas Water Development Board (TWDB). Observation-based naturalized streamflow offers a direct representation of complex hydrological conditions and is less prone to uncertainties than simulation-based estimates. Using the naturalized streamflow as a benchmark, this study quantifies the influence of water management on drought characteristics across 32 streamflow gauges along the mainstems of seven major rivers in Texas by comparing drought conditions under natural and managed conditions. Results indicate that water management has delayed the hydrological drought across Texas’ major rivers by a median of 2.5 months. The impact of the water management on the propagation rate varies across different locations but was found approximately linearly related to the change in the low flow. While the total duration and severity of hydrological droughts were alleviated at more than half of the gauges, average hydrological drought events intensified in most locations due to the significant decrease in drought frequency. Water management was also found to greatly increase spatial variability of drought characteristics across the region. This study enhances our understanding of the influence of human disturbance on hydrological droughts in Texas and similar regions, which is essential for ensuring the sustainable management of water resources and building resilience to droughts in the changing world.

## Journal reference
Yao, L., Ferencz, SB., Sun, N., Yan, H. (2024) Environmental Research Letters [preprint]

## Data reference  
### Input data  
1. Precipitation data from Texas Water Development Board
   * Retrived from the Texas Water Development Board (TWDB) datasets https://waterdatafortexas.org/lake-evaporation-rainfall on March 15, 2024 by author

2. Observed streamflow data from USGS National Water Information System (NWIS)
   * Retrived using a python package, i.e., dataretrieval, https://github.com/DOI-USGS/dataretrieval-python?tab=readme-ov-file
    
3. Naturalized streamflow data from WRAP basin model
   * Retrived from https://www.tceq.texas.gov/permitting/water_rights/wr_technical-resources/wam.html for the FLO file.

4. Streamflow flowline data from National Hydrography Dataset Plus (NHDPlus) Data
   * Retrived from https://www.epa.gov/waterdata/nhdplus-texas-data-vector-processing-unit-12

6. Streamflow gauge drainage area boundary from Hydro Network-Linked Data Index (NLDI)
   * Retrieved from https://waterdata.usgs.gov/blog/nldi-intro/

8. Texas-Gulf basin (HUC2=12) boundary from the National Map developed by USGS
   * Retrived from https://waterdata.usgs.gov/blog/nldi-intro/
   
10. The location of the major reservoirs from Texas Water Development Board
    * Retrieved from https://www.twdb.texas.gov/mapping/gisdata.asp
      
11. The boundary of the Texas from Texas Department of Transportation
    * Retrived from https://gis-txdot.opendata.arcgis.com/datasets/TXDOT::texas-state-boundary/explore?location=30.834886%2C-100.077018%2C6.08

### Output data
Output data for each drought characteristics in the 'plot.csv' under the 'Plot.zip'

## Reproduce my experiment
1. Download 'Observed_Q.zip', 'Naturalized_Q.zip', and 'Precipitation.zip' folders for the input data, and download the 'Plot.zip' for the output data which including all the GIS files for plotting.
2. The 'Observed_Q', 'Naturalized_Q', and 'Precipitation' folders are used for saving and processing the observed streamflow, naturalized flow, and precipitation data, respectively. To facilitate data processing, the data for each gauge in the same river basin are saved in folders named after the river within each of the 'Observed_Q', 'Naturalized_Q', and 'Precipitation' folders. The gauge name list for each river can be found in these river folders. The streamflow gauges in the WRAP FLO file do not appear as USGS gauge numbers; instead, they have ID numbers in the WRAP model. The mapping between the WRAP gauge IDs and the USGS gauge numbers is saved in the gauge name list file.
3. Run 'Observed_Q_USGS.py' to extract observed flow from USGS. 
5. The original FLO file from WRAP model were saved in 'FLO' under the 'Naturalized_Q'. Run 'Natural_Q_WRAP.py' to extract the naturalized flow from FLO file and save in csv format. To facilit data processing, the naturalized Q for each gauge was then saved in separate csv file in the river folder under 'Naturalized_Q'.
6. The origial monthly precipitation data from TWDB was saved in 'all_quads_precipitation_inch.csv' under 'Precipitation'. The area coverage of the gauge's drainage within each quadrangle is saved after the gauge number in each river folder under 'Precipitation'. Run 'Area_Weighted_Precipitation.py' to get the area weighted monthly precipitation for each gauge.
9. Run 'Standardized_Streamflow_Index.py' to calculate the 1-month standardized streamflow index for regualted flow and natual flow at the monthly scale.
10. Run 'M-H_Response_Time.py' to calcualte the meteorological-hydrological drought response time.
11. Run 'M-H_Propagation_Rate.py' to calculate the meteorological-hydrological drought propagation rate.
12. Run 'Meteorological_Drought.py' to identify meteorological drought events.
13. Run 'Hydrological_Drought.py' to identify hydrological drought events, and extract the drought characteristics.
15. Merge all the outputs into one .csv file ('plot.csv') and save in the 'Plot' folder
16. The Texas state boundary, Texas-Gulf basin boundary, river mainstems, reservoir, and gauge station shapefiles are saved in the 'Plot' folder.
17. Use the plotting scripts to plot outputs.

## Reproduce my figures 
Use Fig_#.py to generate Fig. 1 to Fig. 7.


