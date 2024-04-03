import requests

url = "https://jsonplaceholder.typicode.com/posts/1" #https://jsonplaceholder.typicode.com/posts muestra todo el contenido previsto pero /1 mostrara el id=1

payload = {}#datos a enviar
headers = {}#formato o tipo de data

#response = requests.request("GET", url, headers=headers, data=payload)#forma a
response=requests.get(url) #forma b

print(response.text)
print("")
print(response)#<Response [200]>  #el 200 es ok

"""VALIDADOR
if response.status_code==400:
    print(response.text)#convierte la respuest en un string
    print(respone.json())
    respuesta=response.json()
else:
    print("error en la solicitud",response.status_code)              #COMO ES 200 SI PONGO EL VERIFICADOR EN 200 HACIA ARRIBA ARROJARIA ERROR"""

import requests

url = "https://jsonplaceholder.typicode.com/posts/100"

payload = {}#datos a enviar
headers = {}#formato o tipo de dato

#response = requests.request("GET", url, headers=headers, data=payload)
response = requests.get(url)

print("")
print(response)#<Response [200]>

if response.status_code == 200:#200 OK
    #print(response.text) #convierte la respuesta en un string
    print(response.json())#convierte la respuesta en un JSON
    respuesta = response.json()
    print("")
    print(respuesta["title"])
    for clave,valor in respuesta.items():
        print(f"clave{clave}-valor {valor}")
else:
    print("Error en la solicitud",response.status_code)


