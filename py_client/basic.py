import requests
#endpoint = "https://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/"

get_response = requests.get(endpoint,params={"abc":123} ,json={"query":"message"})
print(get_response.text)
print(get_response.json)

#HTTP Requests -> HTML
#REST API Request -> JSON
