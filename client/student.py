import csv
import requests
from pprint import pprint
import os

def get_students(file_path: str) -> list:
    '''get group data'''
    with open(file_path) as f:
        reader = csv.reader(f)
        lines = list(reader)
        students = []
        for line in lines[1:]:
            student = {}
            student['first_name'] = line[0].split()[0]
            if len(line[0].split()) == 2:
                student['last_name'] = line[0].split()[1]
            student['github'] = line[1]
            students.append(student)
            # print(student)

        data = {
            'students': students
        }
        return data
    
def add_students(data):
    data['status'] = 1
    r = requests.post('http://codeschooluzapi.pythonanywhere.com/student/add/', json=data)
    print(r.status_code)
    # r = requests.post('https://codeschoolhomeworkapi.pythonanywhere.com/student/add-students/', json=data)

ls = os.listdir('client/group_data')

for file in ls:
    data = get_students(f'client/group_data/{file}')
    for student in data['students']:
        add_students(student)






def add_new_group(group):
    p = {'name': group, 'course': 1}
    r = requests.post('http://codeschooluzapi.pythonanywhere.com/group/add/', json=p)
    print(r.status_code)
    # r = requests.post('https://codeschoolhomeworkapi.pythonanywhere.com/student/add-new-group/', json=p)

for file in ls:
    add_new_group(file.split('.')[0])
# add_new_group('Python-2022P')
    
# def add_students_to_group(group, data):
#     githubs = [student['github'] for student in data['students']]
#     data = {
#         'group': group,
#         'githubs': githubs
#     }
#     r = requests.post('http://127.0.0.1:8000/student/add-students-to-group/', json=data)
#     # r = requests.post('https://codeschoolhomeworkapi.pythonanywhere.com/student/add-students-to-group/', json=data)
#     return r.status_code
      

# def add_homeworks(homework):
#     data = {
#         'homeworks': homework
#     }
#     r = requests.post('http://127.0.0.1:8000/homework/add-homeworks/', json=data)
#     # r = requests.post('https://codeschoolhomeworkapi.pythonanywhere.com/homework/add-homeworks/', json=data)
#     return r.status_code

    
# def add_homeworks_to_group(group, homeworks):
#     data = {
#         'group': group,
#         'homeworks': homeworks
#     }
#     r = requests.post('http://127.0.0.1:8000/homework/add-homeworks-to-group/', json=data)
#     # r = requests.post('https://codeschoolhomeworkapi.pythonanywhere.com/homework/add-homeworks-to-group/', json=data)
#     return r.status_code


# with open('client/homeworks/homework.csv') as f:
#     homeworks = [homework[0]for homework in list(csv.reader(f))[1:]]

# with open('client/homeworks/groups.csv') as f:
#     groups = [homework[0]for homework in list(csv.reader(f))[1:]]
#     print(groups)
        
    

# for group in groups:     
#     file_path = f'client/group_data/{group}.csv'
#     data = get_students(file_path)

#     # add_students(data)
#     # add_new_group(group)
#     # add_students_to_group(group, data)
#     add_homeworks_to_group(group, homeworks)

