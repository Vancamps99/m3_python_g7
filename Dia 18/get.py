import requests

def obtener_lista_pajaros():
    url = "https://aves.ninjas.cl/api/birds"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Convertir el texto de la respuesta en una variable JSON
      return response.json()
       
    else:
        print("Error en la solicitud:", response.status_code)
        return None

if __name__ == "__main__":
    lista_pajaros = obtener_lista_pajaros()
print("Lista de aves obtenida exitosamente.")#verificador de info obtenida correctamente
