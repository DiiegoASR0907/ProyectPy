import requests

# Realiza una solicitud GET a la API
response = requests.get('https://geoportalgasolineras.es/resources/files/preciosEESS_es.xls')

# Verifica que la solicitud fue exitosa
if response.status_code == 200:
    datos = response.json()
    print(datos)
else:
    print(f"Error: {response.status_code}")
