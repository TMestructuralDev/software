import requests

API_URL = "http://127.0.0.1:8000/api/login/"

def login_request(username, password):
    try:
        response = requests.post(API_URL, data={"username": username, "password": password})
        if response.status_code == 200:
            return {"success": True, "token": response.json().get("token")}
        return {"success": False}
    except requests.exceptions.RequestException:
        return {"success": False}