---
description: Infiltrating water for thirsty ground
---

# Water Box

![Project Logo](.gitbook/assets/logop.png)

### Development tools:

{% hint style="info" %}
Language: Python 3.7.4

Software: OpenGrADS

Libraries: Pygrads, Numpy, Scipy, PIL, Matplotlib, Basemap, Ipython, Pandas
{% endhint %}

### What is the Earth Desertification Problem?

The desertification can be preliminarily understood as a set of phenomena that lead certain areas to become deserts or resemble them.

### What will our project provide?

We aim to provide a prioritization basis for promoting vegetation recovery and conservation actions, as well as optimizing processes such as water infiltration into the soil and promoting better storage and consequent water availability in the region.

#### How many simplified steps do we need to provide this?

1. Data Mining
2. Data Analysis
3. Data Correlation
4. Risk Areas Ranking
5. Finding Optimal Solution Implementation Area
6. Green Infrastructure Choosing

### Where has the dataset been found?

The link below contains the utilized datasets and those respective APIs:

* [Distributed Active Archive Center \(DAAC\) APIs](https://earthdata.nasa.gov/collaborate/open-data-services-and-software/api/daac-apis)

#### The datasets instances looks like these images below:

![Albedo Index](.gitbook/assets/albedo_transp%20%281%29.png)

![Population Density Index](.gitbook/assets/population_density_transp%20%281%29.png)

![Soil Moisture Index](.gitbook/assets/soil_moisture_transp.png)

### How the data gathering and green infrastructures could be integrated in a unique solution?

It is a simple concept which follows the steps mentioned before. First we collect the raw data from NASA's databases, after that this data will go through a "pipeline". The basic function of that pipeline is to gather diferent types of data indexes and combine them to create a new index. Our challenge for the next step is to rank the areas with most desertification risk. Using that information we can priorize some places. Finally when a region is selected, the tool will provide the best place in a determinated radius to implement a green infrastructure. It's important to say here that our tool doesn't determinate the best green infrastructure, instead it shows a point within the radius in which such infrastructure will provide the best results on the desertified area, based in the data.

#### The index calculation

Based in the indexes collected from databases we write a math equation to calculate the desertification index

**Desertification Index \(DI\):** \(ghland\*runoff\*tsoil1\*twlt\) / \(grn\*gwetprof\*qinfil\*tsoil6\)

_Variables that contributes to increase desertification:_

* **ghland:** soil heat
* **runoff:** soil water flow
* **tsoil:** superficial soil temperature
* **twlt:** surface temperature of wilted zone

_Variables that contributes to decrease desertification_**:**

* **evptrns:** transpiration energy flow
* **evpsoil:** exposed soil evaporation energy flow
* **grn:** green fraction
* **gwetprof:** soil humidity
* **qinfil:** soil water infiltration ratio
* **tsoil6:** deep soil temperature

