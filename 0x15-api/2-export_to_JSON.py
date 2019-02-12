#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import json
import requests
from sys import argv
if __name__ == "__main__":
    name = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': argv[1]})
    r = requests.get('https://jsonplaceholder.typicode.com/todos',
                     params={'userId': argv[1]})
    username = name.json()[0].get('username')
    filename = argv[1]+".json"
    dic = {argv[1]: []}
    for task in r.json():
        temp_dic = {"task": task.get('title'), "completed":
                    task.get("completed"), "username": username}
        dic[argv[1]].append(temp_dic)
    with open(filename, 'w') as f:
        json.dump(dic, f)
