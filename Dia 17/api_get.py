import requests,json

url = "https://reqres.in/api/users"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
print("")
if response.status_code == 200:#200 OK
    respuesta= response.json()#GUARDA TODA LA DATA
    user_data=respuesta['data']#USER DATA GUARDA la data
    print((user_data))#Solo los datos
    
else:
    print("Error en la solicitud",response.status_code) 
