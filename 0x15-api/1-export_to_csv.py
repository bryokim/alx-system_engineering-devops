#!/usr/bin/python3
"""
Uses the jsonplaceholder.typicode.com API to return information about
TODO list progess for a given employee ID. The output is written to a
csv file. Name of the file is <user_id>.csv where user_id is the id of
the employee.

Format of the csv file:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import json
import requests
from sys import argv

filename = "{}.csv".format(argv[1])


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

with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    csvwriter.writerows(
        [
            [argv[1], employee_name, task.get("completed"), task.get("title")]
            for task in tasks
        ]
    )
