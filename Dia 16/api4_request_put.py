import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/10"

payload = json.dumps({
  "userId": 1,
  "title": "SCATMAN",
  "body": "SKIRI SKIRI  BOM BOROM BOM"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)


print(response.text)
