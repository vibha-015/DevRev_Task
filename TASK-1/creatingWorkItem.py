import requests
import json


# API endpoint

url = "https://api.devrev.ai/works.create"

# Headers
headers = {
    'Authorization': 'eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzExRmhka0ZYVkU6ZGV2dS8xIiwiZXhwIjoxNzQ0MzgxMDE0LCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL2dvb2dsZS1vYXV0aDJ8MTA5ODQ3MDY1MDg4OTg4MzcxNjE1IiwiaHR0cDovL2RldnJldi5haS9hdXRoMF91c2VyX2lkIjoiZ29vZ2xlLW9hdXRoMnwxMDk4NDcwNjUwODg5ODgzNzE2MTUiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9fZG9uIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzExRmhka0ZYVkUiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9pZCI6IkRFVi0xMUZoZGtGWFZFIiwiaHR0cDovL2RldnJldi5haS9kZXZ1aWQiOiJERVZVLTEiLCJodHRwOi8vZGV2cmV2LmFpL2Rpc3BsYXluYW1lIjoiNG5tMjBpczE3NSIsImh0dHA6Ly9kZXZyZXYuYWkvZW1haWwiOiI0bm0yMGlzMTc1QG5tYW1pdC5pbiIsImh0dHA6Ly9kZXZyZXYuYWkvZnVsbG5hbWUiOiJWSUJIQSIsImh0dHA6Ly9kZXZyZXYuYWkvaXNfdmVyaWZpZWQiOnRydWUsImh0dHA6Ly9kZXZyZXYuYWkvdG9rZW50eXBlIjoidXJuOmRldnJldjpwYXJhbXM6b2F1dGg6dG9rZW4tdHlwZTpwYXQiLCJpYXQiOjE3MTI4NDUwMTQsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwianRpIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzExRmhka0ZYVkU6dG9rZW4vdXY5UlU0am4iLCJvcmdfaWQiOiJvcmdfWEg4THE0eFdPRkNCc0NENiIsInN1YiI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by8xMUZoZGtGWFZFOmRldnUvMSJ9.HVChpEuY3RdNyM1sEFsgkWbGSms5GyKEZHJa52IBBUeORa65CeSwqmbSIcgOr6A-tp9edVYRgpQb_FX8hYJ3jQ59KPFA2vBUVa1nudfDYO5KIfMt82pUIz4wR1r13-1qHjZ-v395LoKr1KrhHTs2NfnLg9b_D7vcUY7LELj-S2jQ-wlE96uiE01GvGsd4mVgptpHNHt1NQaCzxTDj3MIr_GiCfCFLSV_03s2A4epfUslcB0ehH65Sawt8jmRbNM1fWalw1rRipxVtp5UzVgzIdw7N5Lcgnwj3dtyhjRz4vfgQRBCoU2NlT89MgzOHa3YW9KojNuCirUK_J7gFivbsA',
    "Content-Type": "application/json"
}

# Body - JSON data
data = {
    "type": "issue",
    "applies_to_part": "PROD-1",
    "owned_by": ['DEVU-1'],
    "title": "New issue"
}

# Convert dictionary to JSON string
json_data = json.dumps(data)

# Send POST request
response = requests.post(url, headers=headers, data = json_data)

# Check if request was successful
if response.status_code == 200 or response.status_code == 201:
    print("Work item created successfully.")
    print("Response:", response.json())
else:
    print(response.status_code)
    print("Error:", response.text)
    
    