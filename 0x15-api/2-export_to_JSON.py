#!/usr/bin/python3
"""Uses the jsonplaceholder.typicode.com API to return information about
todo list progress for a given employee ID. The output is written into
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
import sys


def get_json_file():
    """Get employee data as a json file"""

    filename = f"{sys.argv[1]}.json"
    base_url = "https://jsonplaceholder.typicode.com"

    employee = requests.get(f"{base_url}/users/{sys.argv[1]}").json()
    tasks = requests.get(f"{base_url}/users/{sys.argv[1]}/todos").json()

    with open(filename, "w") as f:
        data = {
            f"{sys.argv[1]}": [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": employee.get("username"),
                }
                for task in tasks
            ]
        }

        json.dump(data, f)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_json_file()
