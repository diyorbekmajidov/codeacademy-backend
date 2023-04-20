import csv
import requests
from pprint import pprint

with open("./khanacademy/data.csv") as f:
    data = csv.reader(f)

    requests_data = {
            "assignament_id":5,
            "students":[]
        }

    n = 0
    for i in data:
        if n == 0:
            title = i
        if n > 1:
            
            student_name = i[0]

            if i[1].isdigit():
                average_score = i[1]
            else:
                average_score = 0

            if i[2].isdigit():
                percent_competed = i[2]
            else:
                percent_competed = 0

            append_data = {
                    "student_name":student_name,
                    "average_score":average_score,
                    "percent_completed":percent_competed,
                    "question":[]  
                            
                }

                
            for e in range(len(title)):
                question_type = title[e].split(":")[0]
                if i[e].isdigit():
                    scor = i[e]
                    question = {
                        "question_type":question_type,
                        "scor":scor
                    }
                    append_data["question"].append(question)
                elif i[e].isalpha():
                    is_completed = i[e]
                    question = {
                        "question_type":question_type, 
                        "is_completed":is_completed,
                    }
                    append_data["question"].append(question)
                
                
            requests_data["students"].append(append_data)
        n += 1
    r = requests.post('http://127.0.0.1:8000/khanacademy/add_data/', json=requests_data)
    pprint(r.status_code)

        