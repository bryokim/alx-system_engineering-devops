#!/usr/bin/python3
"""
Uses the jsonplaceholder.typicode.com API to return information about
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

filename = "{}.json".format(argv[1])


def fetch_resource(path):
    """Fetch data from the given path.

    Args:
        path (str): Location of the resource.

    Returns:
        Any: Deserializes the data in the response to a suitable
            Python type.
    """
    res = requests.get("https://jsonplaceholder.typicode.com{}".format(path))

    return json.loads(res.text)


employee_name = fetch_resource(f"/users/{argv[1]}").get("name")
tasks = fetch_resource(f"/users/{argv[1]}/todos")

with open(filename, "w") as f:
    data = {
        f"{argv[1]}": [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name,
            }
            for task in tasks
        ]
    }

    json.dump(data, f)
