import requests

BASE_URL = "http://127.0.0.1:8000/api/auth/token/login/"

def login_user(username, password):
    """Envía las credenciales al backend y devuelve el token si es válido."""
    response = requests.post(BASE_URL, data={"username": username, "password": password})

    if response.status_code == 200:
        return {"success": True, "token": response.json().get("auth_token")}
    else:
        return {"success": False, "error": response.json()}