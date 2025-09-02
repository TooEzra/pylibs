import requests
response = requests.get('https://www.kaiandkaro.com/')
print(f"The chief elder says; Status Code: {response.status_code}") #Ask the elder for the status of the village
print(response.text) #Ask the elder to tell us the story of the village
