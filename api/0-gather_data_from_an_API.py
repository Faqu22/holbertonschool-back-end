#!/usr/bin/python3
"""
    This a Python script thatfor a given employee ID, returns information about
        his/her TODO list progress.
"""


import json
import sys
from urllib import request

empId = sys.argv[1]

url = request.urlopen(
    "https://jsonplaceholder.typicode.com/users/{}".format(empId))

info = json.loads(url.read().decode("utf-8"))

url_task = request.urlopen(
    "https://jsonplaceholder.typicode.com/todos?userId={}".format(empId))
tasks = json.loads(url_task.read().decode("utf-8"))

completed = [task for task in tasks if task["completed"]]

print("Employee {} is done with tasks ({}/{}):".
        format(info["name"], len(completed), len(tasks)))
title = [task["title"] for task in completed]
for text in title:
    print("\t {}".format(text))
