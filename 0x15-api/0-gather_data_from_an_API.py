#!/usr/bin/python3
"""
Uses the jsonplaceholder.typicode.com API to return information about
TODO list progess for a given employee ID.
"""

import json
import requests
from sys import argv


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


employee_name = fetch_resource("/users/{}".format(argv[1])).get("name")
tasks = fetch_resource("/users/{}/todos".format(argv[1]))

done_tasks = [task.get("title") for task in tasks if task.get("completed")]

total_tasks = len(tasks)
total_done_tasks = len(done_tasks)

print(
    "Employee {} is done with tasks({}/{})".format(
        employee_name, total_done_tasks, total_tasks
    )
)

for task in done_tasks:
    print("\t {}".format(task))
