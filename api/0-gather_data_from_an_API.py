#!/usr/bin/python3
"""
    This a Python script thatfor a given employee ID, returns information about
        his/her TODO list progress.
"""


if __name__ == "__main__":
    import json
    import sys
    from urllib import request

    empId = sys.argv[1]

    info = json.loads(request.urlopen(
        f"https://jsonplaceholder.typicode.com/users/{empId}").read())

    tasks = json.loads(request.urlopen(
        f"https://jsonplaceholder.typicode.com/todos").read())

    user = [task for task in tasks if task["userId"] == int(empId)]
    completed = [task for task in user if task["completed"]]
    countAll, count = len(user), len(completed)

    print(f"Employee {info['name']} is done with tasks ({count}/{countAll}):")
    title = [task["title"] for task in completed]
    for text in title:
        print(f"\t {text}")
