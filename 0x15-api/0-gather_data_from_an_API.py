#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    users = requests.get(f"{url}/users/{employee_id}").json()

    response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = response.json()
    completed_tasks = [todo.get("title") for todo in todos if todo.get("completed") is True]

    print("Employee {} is done with tasks ({}/{}):".format(users.get("name"),len(completed_tasks), len(todos)))

    [print("\t {}".format(c)) for c in completed_tasks]

