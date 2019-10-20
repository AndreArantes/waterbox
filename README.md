---
description: Infiltrating water for thirsty ground
---

# Water Box

![Project Logo](.gitbook/assets/logop.png)

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

The links below contains the utilized datasets and those respective APIs:

* [Distributed Active Archive Center \(DAAC\) APIs](https://earthdata.nasa.gov/collaborate/open-data-services-and-software/api/daac-apis)
* [Albedo Index - MODIS Web Service](https://modis.ornl.gov/data/modis_webservice_soap.html)
* [Population Density Index - SEDAC REST services](https://sedac.ciesin.columbia.edu/arcgis/rest/services/sedac?_ga=2.68266456.87660087.1571488656-1154313842.1571488656)
* [Soil Moisture Index - NSIDC](https://nsidc.org/api?_ga=2.138969850.87660087.1571488656-1154313842.1571488656)

#### The datasets looks like these images below:

![Albedo Index](.gitbook/assets/albedo_transp%20%281%29.png)

![Population Density Index](.gitbook/assets/population_density_transp%20%281%29.png)

![Soil Moisture Index](.gitbook/assets/soil_moisture_transp.png)

### How the data gathering and green infrastructures could be integrated in a unique solution?

It is a simple concept which follows the steps mentioned before. First we collect the raw data from NASA's databases, after that this data will go through a "pipeline". The basic function of that pipeline is to gather diferent types of data indexes and combine them to create a new index. Our challenge for the next step is to rank the areas with most desertification risk. Using that information we can priorize some places. Finally when a region is selected, the tool will provide the best place in a determinated radius to implement a green infrastructure. It's important to say here that our tool doesn't determinate the best green infrastructure, instead it shows a point within the radius in which such infrastructure will provide the best results on the desertified area, based in the data.

#### The index calculation

Set the math equation here.

#### 

