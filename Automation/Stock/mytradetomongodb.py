import pandas
import json

Excel = pandas.read_excel('mytrade.xlsx', sheet_name='12 17 2022, 07 12 23')
Json = Excel.to_json(orient='records')
print(Json)
out_file = open("JSON.json", "w")
json.dump(Json, out_file, indent = 6)
out_file.close()