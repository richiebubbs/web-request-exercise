print("Requesting some data from the internet...")


import requests
import json
import statistics



#request_url = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products/2.json"
#response = requests.get(request_url)
#print(response.status_code)
#print(response.text)
#response_data = json.loads(response.text)
#print(type(response_data))
#
#print(response_data["name"])
#
#request_url_2 = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products.json"
#response_2 = requests.get(request_url_2)
#response_data_2 = json.loads(response_2.text)
#
#print(response_data_2)
#for p in response_data_2:
#    print("The product ID is: ", p["id"])
#    print("The priduct name is: ", p["name"])

request_url_3 = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/gradebook.json"
response_3 = requests.get(request_url_3)
response_data_3 = json.loads(response_3.text)

students = response_data_3["students"]
#print(students)

#print(response_data_3)
#print(type(response_data_3['finalGrade']))


grades = [i["finalGrade"] for i in students]
avg_grade = statistics.mean(grades)
#
print(avg_grade)



