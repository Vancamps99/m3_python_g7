import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
  "userId": 11,
  "title": "SCATMAN",
  "body": "i' am scatman"
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url,json=payload)
if response.status_code==201:
    print("insercion exitosa")
else :print("error al añadir el post")
print(response.text)

print(requests)