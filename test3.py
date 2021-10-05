import json
import csv

with open('covid_cases.json', 'r') as json_file:
    ourjson = json.load(json_file)
covid_data =ourjson['records']
data_file = open('data.csv', 'w')
csv.writer = csv.writer(data_file)
count = 0
for i in covid_data:
    if count == 0:
        header = i.keys()
