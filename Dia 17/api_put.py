import requests
import json

url = "https://reqres.in/api/users/2"

payload = json.dumps({
  "name": "morpheus",
  "residence": "zion"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)
print("")
if response.status_code == 200:
    updated_user = response.json()
    print(f"Actualizado correctamente:{updated_user}")
else:
    print("ERROR")
    

