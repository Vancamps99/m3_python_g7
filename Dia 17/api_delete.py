import requests
import json

url = "https://reqres.in/api/users/2"

payload = json.dumps({
  "id": 6,
  "email": "tracey.ramos@reqres.in",
  "first_name": "Tracey",
  "last_name": "Ramos",
  "avatar": "https://reqres.in/img/faces/6-image.jpg"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)
if response.status_code == 204:#200 OK
   print("eliminado exitosamente",response.status_code)
    
else:
    print("Error en la solicitud",response.status_code) 
