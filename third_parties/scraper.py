import requests

api_key = "lGzfuUOOlLczL_Trs-K1nA"
headers = {"Authorization": "Bearer " + api_key}
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
params = {"url": "https://www.linkedin.com/in/jeegar-tilak-shah/"}
response = requests.get(api_endpoint, params=params, headers=headers)
print(response.json())
