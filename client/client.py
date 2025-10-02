import requests

BASE_URL = "http://localhost:8080"   


def add(x: int, y: int) -> dict:  
    payload = {"x": x, "y": y}
    response = requests.post(f"{BASE_URL}/add", json=payload)
    response.raise_for_status()  
    return response.json()


def multiply(x: int, y: int) -> dict:
    payload = {"x": x, "y": y}
    response = requests.post(f"{BASE_URL}/multiply", json=payload)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("Add:", add(50, 50))
    print("Multiply:", multiply(50, 2))
