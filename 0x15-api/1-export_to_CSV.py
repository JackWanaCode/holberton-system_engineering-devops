#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import csv
import requests
from sys import argv
if __name__ == "__main__":
    name = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': argv[1]})
    r = requests.get('https://jsonplaceholder.typicode.com/todos',
                     params={'userId': argv[1]})
    filename = argv[1]+".csv"
    username = name.json()[0].get('username')
    with open(filename, mode='w') as file:
        name_writer = csv.writer(file, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_ALL)
        for item in r.json():
            name_writer.writerow([argv[1], username,
                                  item.get('completed'),
                                  item.get('title')])
