import requests
import json
import datetime
import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

url = "https://modis.ornl.gov/rst/api/v1/"
header = {'Accept': 'application/json'}  # Use following for a csv response: header = {'Accept': 'text/csv'}

response = requests.get('https://modis.ornl.gov/rst/api/v1/MCD19A3/subset?latitude=-22.42551&longitude=-45.45702'
                        '&band=Sur_albedo&startDate=A2019201&endDate=A2019201&kmAboveBelow=2&kmLeftRight=2',
                        headers=header)

# Raise an exception if the call returns an erro code
response.raise_for_status()

# dates = json.loads(response.text)['dates']
# bands = json.loads(response.text)['bands']

# modis_dates = [i['modis_date'] for i in dates]
# calendar_dates = [i['calendar_date'] for i in dates]

subset = json.loads(response.text)

'''
data_path = '/home/arantesandre97/PycharmProjects/waterbox/data'
filename = 'MCD19A3.txt'
completeName = os.path.join(data_path, filename)
with open(completeName, 'w') as json_file:
    json.dump(subset, json_file, indent=4, sort_keys=True)
'''

# print(json.dumps(subset, indent=4, sort_keys=True))

# print(json.dumps(bands, indent=4, sort_keys=True))

