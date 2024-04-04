import requests
import json

url = "https://reqres.in/api/users"

payload = json.dumps({
  "first_name": "Ignacio",
  "job": "Profesor"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print("")
if response.status_code == 201:
    created_user = response.json()
    print(f"Usuario creado exitosamente:{created_user}")
    
else:
    print("Error en la solicitud:", response.status_code)
