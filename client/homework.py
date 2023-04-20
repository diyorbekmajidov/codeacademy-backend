import csv
import requests 
from pprint import pprint

url = 'http://codeschooluzapi.pythonanywhere.com/lesson/'


def add_homeworks(homework):
    payload = {
        'name': homework,
        'type': 1,
        'course': 1
    }
    response = requests.post(url+'assignment/add/', json=payload)

    print(response.status_code)


def get_tasks(file_path: str):
    with open(file_path) as csvfile:
        data = list(csv.reader(csvfile))
        homeworks =data[0]
        tasks = data[1:]

        problems = []
        i = 0
        for homework in homeworks:
            t = []
            for task in tasks:
                if task[i] != '':
                    t.append(task[i])

            i += 1
            problems.append({'homework': homework, 'problems': t})

    return problems

            
def add_problems(problems: dict):
    response = requests.post(f'{url}task/add/', json=problems)  
    print(response.status_code)


tasks = get_tasks('client/homeworks/problems.csv')

for task in tasks:
    for problem in task['problems']:
        add_problems({'assignment': task['homework'], 'name': problem, 'level': 'easy'})
