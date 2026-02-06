import requests

BASE_URL = "http://127.0.0.1:8000"


def login(email, password):
    return requests.post(
        f"{BASE_URL}/accounts/login/",
        json={
            "email": email,
            "password": password
        }
    )


def upload_csv(file_path):
    with open(file_path, "rb") as f:
        return requests.post(
            f"{BASE_URL}/api/upload/",
            files={"file": f}
        )
    return response
