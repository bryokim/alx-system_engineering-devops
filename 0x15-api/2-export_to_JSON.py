#!/usr/bin/python3
"""Uses the jsonplaceholder.typicode.com API to return information about
TODO list progress for a given employee ID. The output is written into
a json file. Name of the file is <user_id>.json where user_id is the
employee id.

Format of the json:
    { "USER_ID":
        [
            {
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"
            },
            {
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"
            }, ...
        ]
    }
"""

import json
import requests
from sys import argv

filename = f"{argv[1]}.json"
base_url = "https://jsonplaceholder.typicode.com"

username = requests.get(f"{base_url}/users/{argv[1]}").json().get("username")
tasks = requests.get(f"{base_url}/users/{argv[1]}/todos").json()

with open(filename, "w") as f:
    data = {
        f"{argv[1]}": [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in tasks
        ]
    }

    json.dump(data, f)
