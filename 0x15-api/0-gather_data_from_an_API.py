#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    n = sys.argv[1]
    response = requests.get(url+ "/users/{}".format(n))
    data = response.json()
    employee_name = data['name']
    response = requests.get(url + "/todos?userId={}".format(n))
    todos = response.json()
    completed = [todo for todo in todos if todo['completed']]
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed), len(todos)))
    for task in completed:
        print("\t{}".format(task['title']))

