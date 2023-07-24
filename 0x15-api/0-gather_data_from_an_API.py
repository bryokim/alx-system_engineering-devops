#!/usr/bin/python3
"""Uses the jsonplaceholder.typicode.com API to return information about
TODO list progess for a given employee ID.
"""

import requests
from sys import argv

base_url = "https://jsonplaceholder.typicode.com"

employee_name = requests.get(f"{base_url}/users/{argv[1]}").json().get("name")
tasks = requests.get(f"{base_url}/users/{argv[1]}/todos").json()

done_tasks = [task.get("title") for task in tasks if task.get("completed")]

print(
    "Employee {} is done with tasks({}/{})".format(
        employee_name, len(done_tasks), len(tasks)
    )
)

for task in done_tasks:
    print("\t {}".format(task))
