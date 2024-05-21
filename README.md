[![DOI](https://zenodo.org/badge/265254045.svg)](https://zenodo.org/doi/10.5281/zenodo.10442485)

# Yao_et_al_2024_ERL
**Water Regulation Influence on Hydrological Drought Characteristics in Texas**  
  
Lili Yao<sup>1*</sup>, Stephen B Ferencz<sup>1</sup>, Ning Sun<sup>1</sup>, Hongxiang Yan<sup>1</sup>  
  
<sup>1</sup> Pacific Northwest National Laboratory, Richland, WA., USA  
  
<sup>*</sup> corresponding author: lili.yao@pnnl.gov

## Abstract
The state of Texas in the United States is highly susceptible to drought, and its major rivers are subject to extensive water regulation activities. Water regulation alters streamflow regimes, thereby influencing the propagation processes of drought from meteorological to hydrological types and changing the characteristics of hydrological drought. Nevertheless, the impact of water regulation on drought properties in Texas is not yet fully studied. This study aims to fill this gap by leveraging the extensive observation-based naturalized streamflow dataset constructed by the Texas Water Development Board (TWDB). Observation-based naturalized streamflow offers a direct representation of complex hydrological conditions and is less prone to uncertainties than simulation-based estimates. Using the naturalized streamflow as a benchmark, this study quantifies the influence of water regulation on drought characteristics across 32 streamflow gauges along the main stems of seven major rivers in Texas by comparing drought conditions under natural and water regulation conditions. Results indicate that water regulation has delayed the hydrological drought across Texas’ major rivers by a median of 2.5 months. The impact of the water regulation on the propagation rate varies across different locations but was found approximately linearly related to the change in the low flow. While the total duration and severity of hydrological droughts were alleviated at more than half of the gauges, individual hydrological drought events intensified in most locations due to the significantly decrease in drought frequency. Water management was also found to greatly increase spatial variability of drought characteristics across the region. This study enhances our understanding of the influence of water regulation on hydrological droughts in Texas and similar regions, which is essential for ensuring the sustainable management of water resources and building resilience to droughts in the changing world.

## Using the template
Simply click `Use this template` on the main repository page (shows up to the left of `Clone or download`) and fill in your `Repository name`, the `Description`, select whether you want the repository to be `Public` or `Private`, and leave `Include all branches` unchecked.

## Naming your meta-repository
The following naming conventions should be used when naming your repository:  
- Single author:  `lastname_year_journal`
- Multi author:  `lastname-etal_year_journal`
- Multiple publications in the same journal:  `lastname-etal_year-letter_journal` (e.g., `human-etal_2020-b_nature`)

## Customize your `.gitignore` file
A general `.gitignore` for use with Python or R development is included.  However, you may wish to customize this to the needs of your project.  The `.gitignore` file lets Git know what to push to the remote repository and what needs to be ignored and stay local.

## Suggestions
- Don't bog down your repository with a bunch of raw data.  Instead archive and mint a DOI for your data and provide the reference in this repository with instructions for use.
- Create complete and tested documentation for how to use what is in this repository to reproduce your experiment.

## Creating a minted release for your meta-repository
It is important to version and release your meta-repository as well due to changes that may occur during the publication review process.  If you do not know how to conduct a release on GitHub when linked with Zenodo, please contact chris.vernon@pnnl.gov to get set up.  

## The meta-repository markdown template
A sample meta-repository template is provided in this repository in the file `metarepo_template.md`.  

To use it, do the following:
1. Create the template repository as mentioned above in [Using the template](#using-the-template)
2. Clone your new repository to you local machine
3. Change directories into your new meta-repository directory you just cloned
4. Run `git rm README.md` to delete this file (`README.md`) and commit it using `git commit -m 'remove instructions'`
5. Rename `metarepo_template.md` as `README.md`
6. Run `git add README.md` to stage the new file that will show up on load in your remote GitHub repository
7. Run `git rm metarepo_template.md` to remove the original template
8. Run `git commit -m 'set up new template as readme'` to set the changes
9. Run `git push` to send the changes to your remote GitHub repository
10. Modify the `README.md` file to represent your experiement and use the `add`, `commit`, `push` workflow to update your remote repository
