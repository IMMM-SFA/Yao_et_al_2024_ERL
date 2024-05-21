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

1. Observed streamflow data from USGS
2. Naturalized streamflow data from WAM
3. Precipitation data from Texas Water Development Board  

### Output data



## Code reference ? 
The following naming conventions should be used when naming your repository:  
- Single author:  `lastname_year_journal`
- Multi author:  `lastname-etal_year_journal`
- Multiple publications in the same journal:  `lastname-etal_year-letter_journal` (e.g., `human-etal_2020-b_nature`)

## Reproduce my experiment
Download inputs noted in Boundary_conditions.zip
Run Flopy scripts 'Group_X_flopy_modeling.py' for Scenario Groups 1, 2, and 3.
Use plotting scripts to plot outputs.  

## Reproduce my figures 
Use the .py scripts '#.py' to generate figures for ##. These scripts use processed output provided in #.zip.


