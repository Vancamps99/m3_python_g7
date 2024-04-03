import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

payload = json.dumps({
  "userId": 11,
  "title": "SCATMAN",
  "body": "SKIRI SKIRI  BOM BOROM BOM"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
