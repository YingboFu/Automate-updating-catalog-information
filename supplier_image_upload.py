#!/usr/bin/env python3

import requests
import os

# TODO change the url and path to match the experimental environment
url = "http://146.148.54.168/upload/"
path = 'supplier-data/images'

for filename in os.listdir(path):
    if filename.endswith('.jpeg'):
        with open(os.path.join(path, filename), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            # print(r.status_code)

