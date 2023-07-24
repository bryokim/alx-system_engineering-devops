#!/usr/bin/python3
"""Uses the jsonplaceholder.typicode.com API to return information about
TODO list progress for all employees. The output is exported to
todo_all_employees.json.

Format of the output:
    { "USER_ID":
        [
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
            }, ...
        ]
    }
"""

import json
import requests

filename = "todo_all_employees.json"
base_url = "https://jsonplaceholder.typicode.com"


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
        employee = requests.get(f"{base_url}/users/{i}").json()

        # Exit loop if the employee is not found.
        if not employee:
            break

        tasks = requests.get(f"{base_url}/users/{i}/todos").json()
        data.update(
            {
                f'{i}': [
                    {
                        "username": f'{employee.get("username")}',
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
