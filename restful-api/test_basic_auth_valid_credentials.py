import requests
from requests.auth import HTTPBasicAuth

# Ruta de la API de la aplicación que usaremos para probar la autenticación básica
url = "http://127.0.0.1:5000/basic-protected"

def test_basic_auth_valid_credentials():
    # Usar las credenciales correctas configuradas en el servidor
    response = requests.get(url, auth=HTTPBasicAuth("user1", "password"))

    # Verificar si el estado de la respuesta es 200 (éxito)
    assert response.status_code == 200
    # Verificar si el mensaje en el JSON es correcto
    assert response.json() == {"msg": "Basic Auth: Access Granted"}

if __name__ == "__main__":
    test_basic_auth_valid_credentials()
    print("Test passed: Basic Auth with valid credentials works.")
