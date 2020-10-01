#!/usr/bin/env python3

import os
import requests

# TODO change the url and path to match the experimental environment
url = "http://146.148.54.168/fruits/"
descriptions_directory = 'supplier-data/descriptions'
keys = ['name', 'weight', 'description', 'image_name']

for filename in os.listdir(descriptions_directory):
    if filename.endswith('.txt'):
        count = 0
        dictionary = {'name': "", 'weight': 0, 'description': "", 'image_name': ""}
        with open(os.path.join(descriptions_directory, filename), encoding='utf-8') as file:
            for line in file:
                if keys[count] == 'weight':
                    dictionary[keys[count]] = int(line.split()[0])
                    count += 1
                    continue
                dictionary[keys[count]] = line.strip()
                count += 1
        dictionary['image_name'] = filename.replace('.txt', '.jpeg')

        r = requests.post(url, json=dictionary)
        # print(r.status_code)

