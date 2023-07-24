#!/usr/bin/python3
"""
Uses the jsonplaceholder.typicode.com API to return information about
TODO list progress for all employees. The output is exported to
todo_all_employees.json.

Format of the output:
    { "USER_ID":
        [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            },
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            }, ...
        ],
        "USER_ID":
        [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            },
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            }, ...
        ]
    }
"""

import json
import requests

filename = "todo_all_employees.json"


def fetch_resource(path):
    """Fetch data from the given path.

    Args:
        path (str): Location of the resource.

    Returns:
        Any: Deserializes the data in the response to a suitable
            Python type.
    """
    res = requests.get(f"https://jsonplaceholder.typicode.com{path}")

    return json.loads(res.text)


def get_all_employee_data():
    """Fetch needed data for all employees.

    Returns:
        dict: Dictionary of employee data.
            Format:
            {
                <user_id>: [
                    {
                        "username": "USERNAME",
                        "task": "TASK_TITLE",
                        "completed": TASK_COMPLETED_STATUS
                    }, ...
                ], ...
            }
    """

    data = {}
    i = 1
    while True:
        employee = fetch_resource(f"/users/{i}")

        # Exit loop if the employee is not found.
        if not employee:
            break

        tasks = fetch_resource(f"/users/{i}/todos")
        data.update(
            {
                f'{i}': [
                    {
                        "username": f'{employee.get("name")}',
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                    }
                    for task in tasks
                ]
            }
        )
        i += 1

    return data


with open(filename, "w") as f:
    data = get_all_employee_data()
    json.dump(data, f)
