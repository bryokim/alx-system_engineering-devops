#!/usr/bin/python3
"""Uses the jsonplaceholder.typicode.com API to return information about
todo list progress for all employees. The output is exported to
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
    """Fetch needed data for all employees and write to
    todo_all_employees.json."""

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
                f"{i}": [
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

    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    get_all_employee_data()
