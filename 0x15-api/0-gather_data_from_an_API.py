#!/usr/bin/python3
"""Uses the jsonplaceholder.typicode.com API to return information about
todo list progress for a given employee ID.
"""

import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"


def gather_data():
    """Gather data about a certain user"""

    employee = requests.get(f"{base_url}/users/{sys.argv[1]}").json()
    tasks = requests.get(f"{base_url}/users/{sys.argv[1]}/todos").json()

    done_tasks = [task.get("title") for task in tasks if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee.get("name"), len(done_tasks), len(tasks)
        )
    )

    for task in done_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        gather_data()
