import json
import csv
import math
import pandas as pd

# Replace 'file_path.xlsx' with the actual path to your Excel file.
file_path = 'file.xlsx'

sheetName = "health indicators"
df = pd.read_excel(file_path, sheet_name=sheetName)

arr =[]

for index, row in df.iterrows():
    # 'index' is the row index, 'row' is a pandas Series representing the row data.
    # You can access individual elements using row[column_name].
    suffix=''
    if '%' in row['Indicator Name']:
        suffix = '%'
    description=row['Indicator Description']
    if type(row['Indicator Description']) is not str:
        if math.isnan(row['Indicator Description']):
            description=row['Indicator Name']
        
    arr.append({
    "IndicatorLabelTable": row['Indicator ID'],
    "IndicatorDescription": description,
    "DataKey": row['Indicator Name'],
    "DataSourceName": row['Indicator Source'],
    "DataSourceLink": row['Indicator Source url'],
    "LabelSuffix": suffix,
    "LabelPrefix": "",
    "LabelFormat": "",
    "BinningRange5": [],
    "BinningRangeLarge": [],
    "Categories": [],
    "CategorizeByRanking": False,
    "IsCategorical": False,
    "IsDivergent": False,
    "ScatterPlot": True,
    "Map": True,
    "BarGraph": True,
    "Sizing": True,
    "Color": True,
    "RegionalAggregation": False,
    "SignatureSolution": row['Signature Solutions'].split(','),
    "SSTopics": row['Viva Topics'].split(','),
  })

output_file_path = 'indicators.json'

# Write the JSON object to a file.
with open(output_file_path, 'w') as json_file:
    json.dump(arr, json_file, indent=2)
