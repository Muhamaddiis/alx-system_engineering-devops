#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    
    response = requests.get(f"{url}/users/{employee_id}")
    data = response.json()
    employee_name = data['name']
    
    response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = response.json()
    completed_tasks = [todo for todo in todos if todo['completed']]
    
    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{len(todos)}):")
    
    for task in completed_tasks:
        print(f"\t{task['title']}")
