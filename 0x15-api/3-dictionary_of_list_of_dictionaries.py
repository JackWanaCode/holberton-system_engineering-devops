#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import json
import requests
if __name__ == "__main__":
    all_name = requests.get('https://jsonplaceholder.typicode.com/users')
    dic = {}
    filename = "todo_all_employees.json"
    for name in all_name.json():
        user_id = name.get('id')
        username = name.get('username')
        dic[user_id] = []
        r = requests.get('https://jsonplaceholder.typicode.com/todos',
                          params={'userId': user_id})
        for task in r.json():
            temp_dic = {"task": task.get('title'), "completed":
                        task.get("completed"), "username": username}
            dic[user_id].append(temp_dic)
    with open(filename, 'w') as f:
        json.dump(dic, f)
