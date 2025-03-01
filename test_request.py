import requests
import json

url = "http://127.0.0.1:5000/predict"

data = {
    "Gender": "Male",
    "Married": "Married",
    "ApplicantIncome": 600,
    "LoanAmount": 2000000,
    "Credit_History": 1.0
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

try:
    response_data = response.json()
    print(response_data)
except ValueError:
    print("Response content is not valid JSON:", response.text)
