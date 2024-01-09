# Indicator Metadata Sheets
#### This repo has all the metadata files for all the indicators in UNDP Data Futures Exchange.

## Table of Contents
* [Description of Each File](#section-01)
* [Pages or Apps Where MetaData is Used](#section-04)
* [Installation](#section-07)

## Description of Each File<a name="section-01"></a>

#### [indicatorMetaData.json](https://github.com/UNDP-Data/Indicators-MetaData/blob/main/indicatorMetaData.json)
This metadata sheet describe all the indicator in UNDP Data Futures Exchange. 

To see the list of all the indicator click [here](https://black-water-04176b910.4.azurestaticapps.net/list-indicators). Here users can select a country to see the indicators present for a country. Users can select a region to see the indicators that are aggregated for that region.

To edit this json, use the UI [here](https://black-water-04176b910.4.azurestaticapps.net/edit-metadata). Use the UI to edit meta data for indicators or add new indicators; once the user is done with all the changes user can click the `Download Metadata` button to download the updated json file (name of file downloaded `indicatorMetaData.json`). Once the updates json file is downloaded update the `indicatorMetaData.json` file in this git repo
___

#### [disaggregationMetaData.json](https://github.com/UNDP-Data/Indicators-MetaData/blob/main/disaggregationMetaData.json)
This metadata sheet all the disaggregation and are used in the disaggregated visualization in UNDP Data Futures Exchange. 

To see the list of all the indicator click [here](https://black-water-04176b910.4.azurestaticapps.net/list-indicators). Here users can select a country to see the indicators present for a country. Users can select a region to see the indicators that are aggregated for that region.

To edit this json, use the UI [here](https://black-water-04176b910.4.azurestaticapps.net/edit-disaggregation-metadata). Use the UI to edit meta data for disaggregation or add new disaggregation; once the user is done with all the changes user can click the `Download Disaggregation Metadata` button to download the updated json file (name of file downloaded `disaggregationMetaData.json`). Once the updates json file is downloaded update the `disaggregationMetaData.json` file in this git repo
___

#### [vivaTopicsList.json](https://github.com/UNDP-Data/Indicators-MetaData/blob/main/vivaTopicsList.json)
This json file list the name of all the Viva topics pages. The schema of the json file is `{ vivaTopics: string[] }`. This list is used in Viva Topics dropdown in the [metadata edit application](https://black-water-04176b910.4.azurestaticapps.net/). If the user want to add new Viva topics page they just need to add the new topic to this json and it will get populated in the metadata edit application.
___

#### [subNationDataMetaDataByCountries/{{countryCode}}](https://github.com/UNDP-Data/Indicators-MetaData/tree/main/subNationDataMetaDataByCountries)
These json file list the metadata which affect the sub-national visualization on the country pages on UNDP's DFX. To edit these files please contact the developers. The schema is: 

```
  {
    "indicator_id": string;
    "indicator_name": string;
    "group": string;
    "sourceLayer": string;
    "pmtilesURL": string;
    "hasId": string;
    "countryId": string;
    "regionId": string;
    "useCountryLookup": boolean;
  }
```


## Pages or Apps Where MetaData is Used<a name="section-04"></a>
* [__Access-All-Data-Viz__](https://github.com/UNDP-Data/Access-All-Data-Viz): This metadata sheet is used to populate the indicators in Access All Data App and also the Country SubNational Visualization.
* [__dv-edit-indicators-metadata-fe__](https://github.com/UNDP-Data/dv-edit-indicators-metadata-fe): This repo is used to manage, and edit the metadata sheets. Link to the app: [https://black-water-04176b910.4.azurestaticapps.net/](https://black-water-04176b910.4.azurestaticapps.net/)

## Installation<a name="section-07"></a>
How to download the files and edit

```
git clone https://github.com/UNDP-Data/Indicators-MetaData.git
cd Indicators-MetaData
```
