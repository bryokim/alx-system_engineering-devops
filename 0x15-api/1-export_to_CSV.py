#!/usr/bin/python3
"""Uses the jsonplaceholder.typicode.com API to return information about
TODO list progess for a given employee ID. The output is written to a
csv file. Name of the file is <user_id>.csv where user_id is the id of
the employee.

Format of the csv file:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import requests
import sys

if len(sys.argv) > 1:
    filename = f"{sys.argv[1]}.csv"
    base_url = "https://jsonplaceholder.typicode.com"

    employee = requests.get(f"{base_url}/users/{sys.argv[1]}").json()
    tasks = requests.get(f"{base_url}/users/{sys.argv[1]}/todos").json()

    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        csvwriter.writerows(
            [
                [
                    sys.argv[1],
                    employee.get("username"),
                    task.get("completed"),
                    task.get("title"),
                ]
                for task in tasks
            ]
        )
