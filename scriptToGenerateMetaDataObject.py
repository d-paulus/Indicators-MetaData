import json
import csv
import math
import pandas as pd

# Replace 'file_path.xlsx' with the actual path to your Excel file.
file_path = 'newIndicators.xlsx'

sheetName = "Sheet1"
df = pd.read_excel(file_path, sheet_name=sheetName)

arr =[]

for index, row in df.iterrows():
    # 'index' is the row index, 'row' is a pandas Series representing the row data.
    # You can access individual elements using row[column_name].
    suffix=''
    if '%' in row['indicatorname']:
        suffix = '%'
    description=row['indicatordescription']
    if type(row['indicatordescription']) is not str:
        if math.isnan(row['indicatordescription']):
            description=row['indicatorname']
    
    arr.append({
        "IndicatorLabelTable": row['indicatorname'],
        "id": row['indicatorid'],
        "IndicatorDescription": description,
        "DataKey": row['indicatorname'],
        "DataSourceName": row['indicatorsource'],
        "DataSourceLink": row['indicatorsourceurl'],
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
        "SignatureSolution": row['signaturesolutions'].split(','),
        "SSTopics": row['vivatopics'].split(','),
        "SDGs": [f"SDG {d}" for d in str(row['SDG']).split(',')],
        "Tags": row['Tag'].split(','),
    })

output_file_path = 'indicatorsNew.json'

# Write the JSON object to a file.
with open(output_file_path, 'w') as json_file:
    json.dump(arr, json_file, indent=2)
