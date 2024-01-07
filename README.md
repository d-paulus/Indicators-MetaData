# MetaData Sheets

This repo has the Indicator Meta Data which is used in Access All Data in the Data Futures Platform. Each indicator is defined as a single object in the array. The data structure is:

## Data Structure of an object in Indicator Metadata Sheet

Key | DataType | Description
--- | --- | --- 
IndicatorLabel | `string` | Description of the indicator which is shown in the dropdown and as headings in the graphs
IndicatorDescription | `string` | Long description of the indicator
DataKey | `string` | Name or Key by which the indicator data is stored in the data sheet json
DataSourceName | `string` | Name of the source from which this indicator data is fetched
DataSourceLink | `string` | Web link to the source
LabelSuffix | `string` | Suffix to the data for the indicator when shown on mouseover. For ex if the `LabelSuffix` is `%` and the data for the indicator is `80` then on mouse over the data would be shown as `80 %`
LabelPrefix | `string` | Prefix to the data for the indicator when shown on mouseover. For ex if the `LabelPrefix` is `US$` and the data for the indicator is `80` then on mouse over the data would be shown as `US$ 80`
LabelFormat | `string` | Currently not in used, but needed. Therefor the valuer currently is always _""_
BinningRange5 | `[number, number, number, number]` | An array of 4 numbers defining the domain for threshold scale in bi-variate choropleth map. _If the indicator has categorical data the value of this need to be `[]`_
BinningRangeLarge | `number[]` | An array of  numbers defining the domain for threshold scale in single variate choropleth map. The length of array can vary from 4 to 10. _If the indicator has categorical data the value of this need to be `[]`_
Categories | `number[] or string[]` | An array of  numbers or string defining the categories if the the indicator has categorical data. The length of array can be 5, 7 or 10. _If the indicator is not categorical in nature value of this need to be `[]`_
IsCategorical | `boolean` | Define if the indicator is categorical in nature or not
IsDivergent | `boolean` | Define if the indicator data is divergent in nature or not. This defines the colors that are used for choropleth map. If `true` a divergent color scheme is used otherwise a linear color scheme is used
Sizing | `boolean` | Define if the indicator can be visualized as the size or bubble in scatter plot or as an overlay on the map (generally categorical data and data which can have negative values are not visualized as area)
SignatureSolution | `string[]` | Define the signature solution this indicator is part of
SSTopics | `string[]` | Define the topics this indicator is a part of
id | `string` | This is string by which individual indicator files are stored in github data repo
SDGs | `string[]` | Array of all the sdgs the indicator is related to. _Format of the string is `SDG {Number}`_
Tags | `string[]` | Array of all the tags the indicator is related to

__Example__

```
{
  "IndicatorLabel": "Maternal Mortality Ratio",
  "IndicatorDescription": "The maternal mortality ratio (MMR) is defined as the number of maternal deaths during a given time period per 100,000 live births during the same time period. It depicts the risk of maternal death relative to the number of live births and essentially captures the risk of death in a single pregnancy or a single live birth.",
  "DataKey": "Gender Inequality Index-Maternal mortality ratio (deaths per 100,000 live births)",
  "DataSourceName": "United Nations Development Programme (UNDP)",
  "DataSourceLink": "http://hdr.undp.org/en/content/gender-inequality-index-gii",
  "LabelSuffix": "",
  "LabelPrefix": "",
  "LabelFormat": "",
  "BinningRange5": [
    10,
    100,
    500,
    1000
  ],
  "BinningRangeLarge": [
    10,
    50,
    100,
    200,
    500,
    1000
  ],
  "Categories": [],
  "IsCategorical": false,
  "IsDivergent": false,
  "Sizing": true,
  "RegionalAggregation": true,
  "SignatureSolution": [
    "Poverty and Inequality",
    "Gender"
  ],
  "SSTopics": [
    "Poverty and Inequality Metrics",
    "Building Resilient and Sustainable Systems for Health",
    "Reducing Inequalities and Social Exclusion That Affect Health and Drive Epidemics",
    "Data for Social Norms change and Innovative Policies",
    "Promoting Effective and Inclusive Governance for HIV",
    "Sexual and reproductive health and rights",
    "Gender equality and empowering women and girls in the context of HIV and health"
  ],
  "id": "mmrlatest_gii",
  "SDGs": [
    "SDG 3"
  ],
  "Tags": [
    "Health and HIV"
  ]
}
```
