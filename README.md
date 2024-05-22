[![DOI](https://zenodo.org/badge/265254045.svg)](https://zenodo.org/doi/10.5281/zenodo.10442485)

# Yao_et_al_2024_ERL
**Water Regulation Influence on Hydrological Drought Characteristics in Texas**  
  
Lili Yao<sup>1*</sup>, Stephen B Ferencz<sup>1</sup>, Ning Sun<sup>1</sup>, Hongxiang Yan<sup>1</sup>  
  
<sup>1</sup> Pacific Northwest National Laboratory, Richland, WA., USA  
  
<sup>*</sup> corresponding author: lili.yao@pnnl.gov

## Abstract
The state of Texas in the United States is highly susceptible to drought, and its major rivers are subject to extensive water regulation activities. Water regulation alters streamflow regimes, thereby influencing the propagation processes of drought from meteorological to hydrological types and changing the characteristics of hydrological drought. Nevertheless, the impact of water regulation on drought properties in Texas is not yet fully studied. This study aims to fill this gap by leveraging the extensive observation-based naturalized streamflow dataset constructed by the Texas Water Development Board (TWDB). Observation-based naturalized streamflow offers a direct representation of complex hydrological conditions and is less prone to uncertainties than simulation-based estimates. Using the naturalized streamflow as a benchmark, this study quantifies the influence of water regulation on drought characteristics across 32 streamflow gauges along the main stems of seven major rivers in Texas by comparing drought conditions under natural and water regulation conditions. Results indicate that water regulation has delayed the hydrological drought across Texas’ major rivers by a median of 2.5 months. The impact of the water regulation on the propagation rate varies across different locations but was found approximately linearly related to the change in the low flow. While the total duration and severity of hydrological droughts were alleviated at more than half of the gauges, individual hydrological drought events intensified in most locations due to the significantly decrease in drought frequency. Water management was also found to greatly increase spatial variability of drought characteristics across the region. This study enhances our understanding of the influence of water regulation on hydrological droughts in Texas and similar regions, which is essential for ensuring the sustainable management of water resources and building resilience to droughts in the changing world.

## Journal reference
Yao, L., Ferencz, SB., Sun, N., Yan, H. (2024) Environmental Research Letters [preprint]

## Data reference  
### Input data  
1.Precipitation data from Texas Water Development Board
   * Retrived from the Texas Water Development Board (TWDB) datasets https://waterdatafortexas.org/lake-evaporation-rainfall on March 15, 2024 by author
     
2. Observed streamflow data from USGS
   * Retrived from the National Water Information System (NWIS) using a python package, i.e., dataretrieval, https://github.com/DOI-USGS/dataretrieval-python?tab=readme-ov-file
     
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

### Output data
Output data for each drought characteristics in the Drought_results.zip


## Reproduce my experiment
1. Download inputs noted in Boundary_conditions.zip
2. Run Area_Weighted_Precipitation.py to get the area weighted monthly precipitation for each gauge.
3. Run Observed_Q_USGS.py to extract the observed flow from USGS for each gauge.
4. Run Natural_Q_WRAP.py to extract the naturalized flow from FLO file from WRAP models.
5. Run Standardized_Streamflow_Index.py to calculate the 1-month standardized streamflow index for regualted flow and natual flow at the monthly scale.
6. Run M-H_Response_Time.py to calcualte the meteorological-hydrological drought response time.
7. Run M-H_Propagation_Rate.py to calculate the meteorological-hydrological drought propagation rate.
8. Run Meteorological_Drought.py to identify meteorological drought events.
9. Run Hydrological_Drought.py to identify hydrological drought events, and extract the drought characteristics.
10. Merge all the outputs into one .csv file (plot.csv), and use plotting scripts to plot outputs.  

## Reproduce my figures 
Use the .py scripts '#.py' to generate figures for ##. These scripts use processed output provided in #.zip.


