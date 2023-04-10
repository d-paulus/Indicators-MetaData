# Indicators-MetaData

This repo has the Indicator Meta Data which is used in Access All Data in the Data Futures Platform (https://data.undp.org/explore-all-data/). Each indicator is defined as a single object in the array. The data structure is:

## Data Structure of an object

Key | DataType | Description
--- | --- | --- 
Indicator | `string` | Short description of the indicator
IndicatorLabelTable | `string` | Describtion of the indicator which is shown in the dropdown and as headings in the graphs
IndicatorDescription | `string` | Long description of the indicator
DataKey | `string` | Name or Key by which the indicator data is stored in the data sheet json
DataSourceName | `string` | Name of the source from which this indicator data is fetched
DataSourceLink | `string` | Weblink to the source
LabelSuffix | `string` | Suffix to the data for the indicator when shown on mouseover. For ex if the `LabelSuffix` is `%` and the data for the indicator is `80` then on mouse over the data would be shown as `80 %`
LabelPrefix | `string` | Prefix to the data for the indicator when shown on mouseover. For ex if the `LabelPrefix` is `US$` and the data for the indicator is `80` then on mouse over the data would be shown as `US$ 80`
LabelFormat | `string` | Currently not in used, but needed. Therefor the valuer currently is always _""_
BinningRange5 | `[number, number, number, number]` | An array of 4 numbers defining the domain for threshold scale in bivariate choropleth map. _If the indicator has categorical data the value of this need to be `[]`_
BinningRangeLarge | `number[]` | An array of  numbers defining the domain for threshold scale in single variate choropleth map. The length of array can vary from 4 to 10. _If the indicator has categorical data the value of this need to be `[]`_
Categories | `number[] or string[]` | An array of  numbers or string defining the categories if the the indicator has categorical data. The length of array can be 5, 7 or 10. _If the indicator is not categorical in nature value of this need to be `[]`_
CategorizeByRanking | `boolean` | Currently not in use
IsCategorical | `boolean` | Define if the indicator is categorical in nature or not
IsDivergent | `boolean` | Define if the indicator data is divergent in nature or not. This defines the colors that are used for choropleth map. If `true` a divergentcolor scheme is used otherwise a linear color schame is used
ScatterPlot | `boolean` | Define if the indicator can be visualized in scatterplot (generally categorical data are not visualized as scatter plot)
Map | `boolean` | Define if the indicator can be visualized as color in choropleth map
BarGraph | `boolean` | Define if the indicator can be visualized as bars in bar graph (generally categorical data are not visualized as scatter plot)
Sizing | `boolean` | Define if the indicator can be visualized as the size or bubble in scatterplot or as an overlay on the map (generally categorical data and data which can have negative values are not visualized as area)
Color | `boolean` | Define if the indicator can be visualized as color of bubbles in scatterplot and bar chart (only categorical data are visualized as colors in scatter plot and bar chart)
SignatureSolution | `string[]` | Define the signature solution this indicator is part of
SSTopics | `string[]` | Define the topics this indicator is a part of

__Example__

```
{
  "Indicator": "Gender Inequality Index-Population with at least some secondary education, female (% ages 25 and older)",
  "IndicatorLabelTable": "Gender inequality index, female population with secondary education",
  "IndicatorDescription": "Percent of females ages 25 and older with some secondary education",
  "DataKey": "Gender Inequality Index-Population with at least some secondary education, female (% ages 25 and older)",
  "DataSourceName": "Undp, gender inequality index",
  "DataSourceLink": "http://hdr.undp.org/en/content/gender-inequality-index-gii",
  "LabelSuffix": "%",
  "LabelPrefix": "",
  "LabelFormat": "",
  "BinningRange5": [
    20,
    40,
    60,
    80
  ],
  "BinningRangeLarge": [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90
  ],
  "Categories": [],
  "CategorizeByRanking": false,
  "IsCategorical": false,
  "IsDivergent": false,
  "ScatterPlot": true,
  "Map": true,
  "BarGraph": true,
  "Sizing": true,
  "Color": true,
  "SignatureSolution": [],
  "SSTopics": []
}
```
